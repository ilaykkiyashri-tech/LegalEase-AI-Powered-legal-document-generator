import io
import os
import re

from docx import Document
from docx.shared import Inches, Pt
from fpdf import FPDF

LOGO_PATH = os.getenv("LOGO_PATH", "Image/Logo.png")
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."


def sanitize_text(text: str) -> str:
    """Removes special/typographic characters that break PDF/DOCX rendering."""
    if not text:
        return ""
    replacements = {
        "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-",
        "\u2026": "...",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    text = re.sub(r"[^\x00-\x7F]+", "", text)
    return text.strip()


def _split_terms(terms: str):
    return [t.strip() for t in terms.split(";") if t.strip()]


def format_docx(text: str, doc_type: str, parties: str = "", terms: str = "", dates: str = "") -> bytes:
    """Builds a branded Word document from generated text."""
    text = sanitize_text(text)
    doc = Document()

    if os.path.exists(LOGO_PATH):
        try:
            doc.add_picture(LOGO_PATH, width=Inches(1.5))
        except Exception:
            pass

    title = doc.add_heading(doc_type or "Legal Document", level=1)
    title.alignment = 1

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("##"):
            doc.add_heading(line.replace("#", "").strip(), level=2)
        else:
            p = doc.add_paragraph(line)
            for run in p.runs:
                run.font.name = "Times New Roman"
                run.font.size = Pt(11)

    term_list = _split_terms(terms)
    if term_list:
        doc.add_heading("Key Terms", level=2)
        table = doc.add_table(rows=1, cols=1)
        try:
            table.style = "Light Grid Accent 1"
        except KeyError:
            pass
        table.rows[0].cells[0].text = "Term"
        for t in term_list:
            row = table.add_row()
            row.cells[0].text = t

    doc.add_paragraph()
    footer = doc.add_paragraph(FOOTER_TEXT)
    footer.alignment = 1

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


class _BrandedPDF(FPDF):
    title_text = "Legal Document"
    def multi_cell(self, w, h=None, text="", *args, **kwargs):
        kwargs.setdefault("new_x", "LMARGIN")
        kwargs.setdefault("new_y", "NEXT")
        return super().multi_cell(w, h, text, *args, **kwargs)

    def header(self):
        if os.path.exists(LOGO_PATH):
            try:
                self.image(LOGO_PATH, x=(210 - 30) / 2, y=8, w=30)
                self.ln(18)
            except Exception:
                self.ln(5)
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, self.title_text, align="C")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, FOOTER_TEXT, align="C")


def format_pdf(text: str, doc_type: str, terms: str = "") -> bytes:
    """Builds a branded PDF from generated text."""
    text = sanitize_text(text)
    pdf = _BrandedPDF()
    pdf.title_text = doc_type or "Legal Document"
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)

    for line in text.split("\n"):
        line = line.strip()
        if not line:
            pdf.ln(4)
            continue
        if line.startswith("##"):
            pdf.set_font("Helvetica", "B", 12)
            pdf.multi_cell(0, 8, line.replace("#", "").strip())
            pdf.set_font("Helvetica", size=11)
        else:
            pdf.multi_cell(0, 7, line)

    term_list = _split_terms(terms)
    if term_list:
        pdf.set_font("Helvetica", "B", 12)
        pdf.multi_cell(0, 8, "Key Terms")
        pdf.set_font("Helvetica", size=11)
        for t in term_list:
            pdf.multi_cell(0, 7, f"- {t}")

    output = pdf.output(dest="S")
    if isinstance(output, str):
        return output.encode("latin-1")
    return bytes(output)


def format_html_preview(text: str) -> str:
    """Converts generated text into styled HTML for the Streamlit preview card."""
    text = sanitize_text(text)
    lines_html = []
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("##"):
            heading = line.replace("#", "").strip()
            lines_html.append(f"<h4 style='color:#f0f0f0;margin:10px 0 4px;'>{heading}</h4>")
        else:
            lines_html.append(f"<p style='color:#dddddd;margin:4px 0;'>{line}</p>")
    return "".join(lines_html)
