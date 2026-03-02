/**
 * Consumer Agent — Service Worker
 * 
 * This is the "consumer side" of the Agent-as-Download.
 * It registers in the browser, fetches the governance protocol,
 * asks the provider agent to generate an experience, and serves it.
 * 
 * This service worker IS the agent's local presence.
 */

const PROVIDER_URL = self.__PROVIDER_URL || 'https://agent-demo.sovereign-streams.workers.dev';
const CACHE_NAME = 'sovereign-agent-v1';
const GENERATION_TIMEOUT_MS = 60000;

// State
let governanceProtocol = null;
let consumerPreferences = {};
let generatedPages = {};

// Install — take over immediately
self.addEventListener('install', (event) => {
  console.log('[Agent] 🤖 Consumer agent installing...');
  self.skipWaiting();
});

// Activate — claim all clients
self.addEventListener('activate', (event) => {
  console.log('[Agent] 🤖 Consumer agent activated');
  event.waitUntil(self.clients.claim());
});

// Listen for messages from the main page
self.addEventListener('message', (event) => {
  const { type, data } = event.data || {};
  
  if (type === 'SET_PROVIDER_URL') {
    self.__PROVIDER_URL = data.url;
    console.log('[Agent] Provider URL set to:', data.url);
  }
  
  if (type === 'SET_PREFERENCES') {
    consumerPreferences = data.preferences || {};
    console.log('[Agent] Preferences updated:', consumerPreferences);
  }

  if (type === 'GENERATE') {
    // Trigger experience generation
    generateExperience(event.source);
  }

  if (type === 'GET_STATUS') {
    event.source.postMessage({
      type: 'STATUS',
      data: {
        hasGovernance: !!governanceProtocol,
        hasCachedExperience: Object.keys(generatedPages).length > 0,
        preferences: consumerPreferences,
        providerName: governanceProtocol?.provider_name || null,
      }
    });
  }
});

async function fetchGovernance(providerUrl) {
  const url = providerUrl || self.__PROVIDER_URL || PROVIDER_URL;
  console.log('[Agent] 📋 Fetching governance protocol from:', url);
  
  const res = await fetch(`${url}/governance`);
  if (!res.ok) throw new Error(`Governance fetch failed: ${res.status}`);
  
  governanceProtocol = await res.json();
  console.log('[Agent] ✅ Governance protocol received:', governanceProtocol.provider_name);
  
  // Validate governance — the agent's first act of sovereignty
  validateGovernance(governanceProtocol);
  
  return governanceProtocol;
}

function validateGovernance(gov) {
  // The consumer agent checks the provider's governance for red flags
  const forbidden = gov.experience_guidance?.forbidden_patterns || [];
  console.log('[Agent] 🛡️ Governance validated. Forbidden patterns:', forbidden.length);
  
  // Check for required features
  const required = (gov.experience_guidance?.core_features || [])
    .filter(f => f.priority === 'required');
  console.log('[Agent] 📋 Required features:', required.map(f => f.id).join(', '));
  
  return true;
}

async function generateExperience(client) {
  const providerUrl = self.__PROVIDER_URL || PROVIDER_URL;
  
  try {
    // Step 1: Fetch governance if we don't have it
    if (!governanceProtocol) {
      notifyClient(client, 'AGENT_STATUS', { phase: 'governance', message: 'Fetching governance protocol...' });
      await fetchGovernance(providerUrl);
      notifyClient(client, 'AGENT_STATUS', { phase: 'governance_done', message: `Connected to ${governanceProtocol.provider_name}`, governance: governanceProtocol });
    }

    // Step 2: Negotiate — check governance against preferences
    notifyClient(client, 'AGENT_STATUS', { phase: 'negotiating', message: 'Negotiating experience with provider agent...' });
    
    // Step 3: Request experience generation from provider agent
    notifyClient(client, 'AGENT_STATUS', { phase: 'generating', message: 'Provider agent is generating your experience...' });
    
    const res = await fetch(`${providerUrl}/agent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        action: 'generate_experience',
        preferences: consumerPreferences,
      }),
    });

    if (!res.ok) {
      const err = await res.text();
      throw new Error(`Generation failed: ${res.status} — ${err}`);
    }

    const result = await res.json();
    
    // Step 4: Cache the generated experience
    generatedPages['main'] = result.html;
    const cache = await caches.open(CACHE_NAME);
    await cache.put(new Request('/experience'), new Response(result.html, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' },
    }));
    
    console.log('[Agent] ✨ Experience generated and cached');
    
    // Step 5: Notify the launcher
    notifyClient(client, 'EXPERIENCE_READY', {
      html: result.html,
      generated_at: result.generated_at,
      model: result.model,
      governance: governanceProtocol,
    });
    
  } catch (err) {
    console.error('[Agent] ❌ Generation failed:', err);
    notifyClient(client, 'AGENT_ERROR', { error: err.message });
  }
}

function notifyClient(client, type, data) {
  if (client && client.postMessage) {
    client.postMessage({ type, data });
  } else {
    // Broadcast to all clients
    self.clients.matchAll().then(clients => {
      clients.forEach(c => c.postMessage({ type, data }));
    });
  }
}

// Intercept fetches — serve generated experience from cache
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  
  // Serve cached experience for /experience path
  if (url.pathname === '/experience') {
    event.respondWith(
      caches.match(event.request).then(cached => {
        if (cached) return cached;
        return new Response('<html><body><h1>No experience generated yet</h1><p>Return to the launcher and click "Activate Agent".</p></body></html>', {
          headers: { 'Content-Type': 'text/html' },
        });
      })
    );
    return;
  }
  
  // Everything else — pass through normally
  event.respondWith(fetch(event.request));
});
