# Phase 5: Project Development

## 5.1 Legal Document Generation

**`legalEaseAPI/routes.py`**
```python
from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
gemini_generator = GeminiDocumentGenerator()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    response = gemini_generator.generate_document(
        request.document_type,
        request.parties,
        request.terms,
        request.dates
    )
    return {"document": response}
```

**`ai_core/gemini_generator.py`**
```python
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiDocumentGenerator:
    def __init__(self, model_name="gemini-1.5-pro"):
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type, parties, terms, dates):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            f"Ensure formal legal structure with multiple sections and legal clauses."
        )
        response = self.model.generate_content(prompt)
        return response.text
```

## 5.2 FastAPI Backend Entry Point

**`legalEaseAPI/main.py`**
```python
from fastapi import FastAPI
from legalEaseAPI.routes import router

app = FastAPI(title="LegalEase - AI Legal Document Generator")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to LegalEase AI Legal Document Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## 5.3 Streamlit Frontend

**`frontend/app.py`** (key excerpts)
```python
import streamlit as st
import requests

st.set_page_config(page_title="LegalEase", layout="centered")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(WEB_LOGO_PATH, use_container_width=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

document_type = st.text_input("Document Type")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

if st.button("Generate Document"):
    response = requests.post("http://localhost:8000/generate", json={
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "dates": dates
    })
    generated_text = sanitize_text(response.json()["document"])
    st.session_state.generated_text = generated_text

if st.session_state.get("show_edit"):
    edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
    st.session_state.generated_text = edited_text

st.download_button("Download as .TXT", data=generated_text, ...)
st.download_button("Download as .DOCX", data=format_docx(generated_text, document_type), ...)
st.download_button("Download as .PDF", data=format_pdf(generated_text, document_type), ...)
```

## 5.4 Core Formatting Utilities
- `sanitize_text(text)` — strips special characters/typographic quotes
- `format_docx(text, doc_type)` — python-docx: embeds logo, formats titles/paragraphs, converts semicolon-separated terms into a table
- `format_pdf(text, doc_type)` — FPDF: center-aligned logo, bold section headings, bullet-style terms, custom header/footer
- `format_html_preview(text)` — converts generated text into a styled HTML block for in-app display

## Development Notes
- Dependencies: `fastapi`, `uvicorn`, `streamlit`, `python-docx`, `fpdf`, `Pillow`, `requests`, `google-generativeai`, `python-dotenv`
- Gemini API key is read from `.env` via `GEMINI_API_KEY`
- All generated content passes through `sanitize_text` before formatting/export
