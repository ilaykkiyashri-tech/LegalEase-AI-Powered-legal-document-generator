# Phase 3: Project Design

## System Architecture

```
User Interface (Streamlit) → FastAPI Backend (main.py) → Document Generator
(gemini_generator.py) → Gemini 1.5 API → Formatted Output (.txt, .docx, .pdf)
```

### Components
- **Frontend:** Streamlit — collects user input, shows document preview, handles editing and downloads
- **Backend:** FastAPI (`main.py`, `routes.py`) — receives JSON payload, routes to the AI generator, returns generated text
- **AI Core:** `ai_core/gemini_generator.py` — builds the prompt and calls Gemini's `generate_content`
- **Formatting Modules:** DOCX, PDF, and HTML-preview generators

## Data Flow
1. User fills in document type, parties, terms, and effective date in Streamlit.
2. Streamlit sends a POST request to `http://localhost:8000/generate` with a JSON payload.
3. FastAPI validates the payload against the `DocumentRequest` Pydantic model.
4. `routes.py` calls `GeminiDocumentGenerator.generate_document(...)`.
5. `gemini_generator.py` builds a structured prompt and calls Gemini's `generate_content`.
6. The generated text is returned to the frontend, sanitized, and rendered as a styled HTML preview.
7. User can edit the text inline, then export as .TXT, .DOCX, or .PDF.

## API Design
**Endpoint:** `POST /generate`

Request body (`DocumentRequest`):
```python
class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str
```

Response:
```json
{ "document": "<generated legal document text>" }
```

## Application Folder Structure
```
LEGALEASE/
├── ai_core/
│   ├── gemini_generator.py
│   └── generator.py
├── docs/
├── frontend/
│   └── app.py
├── Image/
│   ├── inverseLogo.png
│   └── Logo.png
├── legalEaseAPI/
│   ├── main.py
│   └── routes.py
├── venv/
├── .env
├── config.py
├── requirements.txt
└── run.sh
```

## Core Utility Functions (Design)
- `sanitize_text(text)` — removes special characters/typographic quotes for clean formatting
- `format_docx(text, doc_type)` — builds a Word doc with logo, titles, and a terms table (python-docx)
- `format_pdf(text, doc_type)` — builds a branded PDF with header/footer (FPDF)
- `format_html_preview(text)` — converts text into styled HTML for in-app preview

## UI Design Notes
- Centered layout, company logo at top (three-column layout via `st.columns`)
- Input fields: Document Type, Parties Involved, Terms & Conditions, Effective Date
- Buttons: "Generate Document," "Edit Document," and three download buttons (TXT/DOCX/PDF)
- Dark-themed, scrollable HTML preview card
