#!/usr/bin/env python3
"""
Generate PDF from LAWS-OF-TRUST.md markdown file.
Properly handles all law content including body paragraphs.
"""

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, PageTemplate, Frame, KeepTogether
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black
from datetime import datetime

def read_markdown(filepath):
    """Read the markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def extract_preface(content):
    """Extract preface section."""
    match = re.search(r'## Preface: Why This Book Exists\n\n(.*?)\n---\n\n## The Laws', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def extract_laws(content):
    """Extract all 48 laws from markdown."""
    laws = []

    # Split by law headers
    law_pattern = r'### Law (\d+)\n\n(.*?)(?=### Law \d+|$)'
    matches = re.finditer(law_pattern, content, re.DOTALL)

    for match in matches:
        law_num = int(match.group(1))
        law_content = match.group(2)

        # Extract Law of Power section
        power_match = re.search(r'\*\*Law of Power:\*\* \*(.*?)\*\.?\n(.*?)(?=\*\*Law of Trust:|$)', law_content, re.DOTALL)

        power_title = ""
        power_description = ""
        if power_match:
            power_title = power_match.group(1).strip()
            power_description = power_match.group(2).strip()

        # Extract Law of Trust section
        trust_match = re.search(r'\*\*Law of Trust:\*\* \*\*\*(.*?)\*\*\*\.?\n(.*?)(?=\*\*The historical lesson:|In Web 4\.0:|$)', law_content, re.DOTALL)

        trust_title = ""
        trust_description = ""
        if trust_match:
            trust_title = trust_match.group(1).strip()
            trust_description = trust_match.group(2).strip()

        # Extract commentary (body text between Law of Trust and lessons)
        commentary_match = re.search(r'\*\*Law of Trust:\*\*.*?\n\n(.*?)(?=\*\*The historical lesson:|In Web 4\.0:|$)', law_content, re.DOTALL)
        commentary = ""
        if commentary_match:
            full_section = commentary_match.group(1)
            # Remove the Law of Trust title line
            lines = full_section.split('\n')
            comment_lines = []
            for line in lines:
                if line.startswith('***') or 'Law of Trust' in line:
                    continue
                if line.strip():
                    comment_lines.append(line.strip())
            commentary = '\n\n'.join(comment_lines)

        # Extract historical lesson
        historical_match = re.search(r'\*\*The historical lesson:\*\*(.*?)(?=\*\*In Web 4\.0:|$)', law_content, re.DOTALL)
        historical = ""
        if historical_match:
            historical = historical_match.group(1).strip()

        # Extract Web 4.0 section
        web40_match = re.search(r'\*\*In Web 4\.0:\*\*(.*?)$', law_content, re.DOTALL)
        web40 = ""
        if web40_match:
            web40 = web40_match.group(1).strip()

        laws.append({
            'number': law_num,
            'power_title': power_title,
            'power_description': power_description,
            'trust_title': trust_title,
            'trust_description': trust_description,
            'commentary': commentary,
            'historical': historical,
            'web40': web40,
            'raw_content': law_content
        })

    return laws

def clean_text(text):
    """Remove markdown formatting from text."""
    # Remove markdown bold, italic, bold-italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'\1', text)  # ***bold italic***
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)      # **bold**
    text = re.sub(r'\*(.*?)\*', r'\1', text)          # *italic*
    text = re.sub(r'~~(.*?)~~', r'\1', text)          # ~~strikethrough~~
    text = re.sub(r'`(.*?)`', r'\1', text)            # `code`
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def create_pdf(markdown_path, pdf_path):
    """Create PDF from markdown."""
    content = read_markdown(markdown_path)
    preface = extract_preface(content)
    laws = extract_laws(content)

    print(f"Found {len(laws)} laws")

    # Create PDF document
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    # Define styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=60,
        fontName='Helvetica-Bold',
        textColor=black,
        alignment=TA_CENTER,
        spaceAfter=0.3*inch
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        fontName='Helvetica',
        textColor=black,
        alignment=TA_CENTER,
        spaceAfter=0.2*inch
    )

    author_style = ParagraphStyle(
        'Author',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Times-Roman',
        alignment=TA_CENTER,
        spaceAfter=0.1*inch
    )

    law_header_style = ParagraphStyle(
        'LawHeader',
        parent=styles['Heading2'],
        fontSize=16,
        fontName='Helvetica-Bold',
        textColor=black,
        spaceAfter=0.2*inch,
        spaceBefore=0.2*inch
    )

    power_label_style = ParagraphStyle(
        'PowerLabel',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        textColor=HexColor('#8B4513'),  # Dark red/brown
        spaceAfter=0.1*inch
    )

    trust_label_style = ParagraphStyle(
        'TrustLabel',
        parent=styles['Normal'],
        fontSize=11,
        fontName='Helvetica-Bold',
        textColor=HexColor('#2d8a6e'),  # Green
        spaceAfter=0.1*inch
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10.5,
        fontName='Times-Roman',
        alignment=TA_JUSTIFY,
        spaceAfter=0.15*inch,
        leading=13
    )

    section_label_style = ParagraphStyle(
        'SectionLabel',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Bold',
        textColor=black,
        spaceAfter=0.08*inch,
        spaceBefore=0.12*inch
    )

    # Build story
    story = []

    # Title page
    story.append(Spacer(1, 1*inch))
    story.append(Paragraph("48", title_style))
    story.append(Paragraph("LAWS OF TRUST", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("A Reversal of the Laws of Power — and the Spirit of the Next Economy", subtitle_style))
    story.append(Spacer(1, 0.4*inch))
    story.append(Paragraph("Paul Diehl", author_style))
    story.append(Paragraph("March 5, 2026", author_style))
    story.append(PageBreak())

    # Preface page
    if preface:
        story.append(Paragraph("Preface: Why This Book Exists", law_header_style))
        preface_text = clean_text(preface)
        # Split preface into paragraphs
        for para in preface_text.split('\n\n'):
            if para.strip():
                story.append(Paragraph(para.strip(), body_style))
        story.append(PageBreak())

    # Law pages
    for law in laws:
        # Law header
        story.append(Paragraph(f"Law {law['number']}", law_header_style))

        # Law of Power section
        if law['power_title']:
            story.append(Paragraph("Law of Power", power_label_style))
            power_text = f"{clean_text(law['power_title'])}. {clean_text(law['power_description'])}"
            story.append(Paragraph(power_text, body_style))

        # Law of Trust section
        if law['trust_title']:
            story.append(Paragraph("Law of Trust", trust_label_style))
            trust_text = clean_text(law['trust_title'])
            story.append(Paragraph(trust_text, body_style))

        # Commentary
        if law['commentary']:
            commentary_clean = clean_text(law['commentary'])
            for para in commentary_clean.split('\n\n'):
                if para.strip():
                    story.append(Paragraph(para.strip(), body_style))

        # Historical lesson
        if law['historical']:
            story.append(Paragraph("The historical lesson", section_label_style))
            historical_clean = clean_text(law['historical'])
            for para in historical_clean.split('\n\n'):
                if para.strip():
                    story.append(Paragraph(para.strip(), body_style))

        # Web 4.0 section
        if law['web40']:
            story.append(Paragraph("In Web 4.0", section_label_style))
            web40_clean = clean_text(law['web40'])
            for para in web40_clean.split('\n\n'):
                if para.strip():
                    story.append(Paragraph(para.strip(), body_style))

        # Page break between laws (except last)
        if law['number'] < 48:
            story.append(PageBreak())

    # Custom page template with page numbers
    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            canvas.Canvas.__init__(self, *args, **kwargs)
            self.page_count = 0

        def showPage(self):
            self.page_count += 1
            # Draw page number at bottom center
            self.setFont("Times-Roman", 10)
            page_width = letter[0]
            self.drawCentredString(page_width / 2, 0.4*inch, str(self.page_count))
            canvas.Canvas.showPage(self)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generated: {pdf_path}")

if __name__ == "__main__":
    markdown_file = "/sessions/bold-modest-shannon/mnt/projects/sovereign-streams/web4/LAWS-OF-TRUST.md"
    pdf_file = "/sessions/bold-modest-shannon/mnt/projects/sovereign-streams/web4/LAWS-OF-TRUST.pdf"

    create_pdf(markdown_file, pdf_file)
