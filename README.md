# LegalEase — AI-Powered Legal Document Generator

LegalEase generates customizable, editable legal documents (employment contracts, NDAs, lease agreements, and more) from simple structured inputs, using Google's Gemini model, with export to **.TXT**, **.DOCX**, and **.PDF**.

Built with **FastAPI** (backend), **Streamlit** (frontend), and the **Google Generative AI SDK** (Gemini).

## Project Phases
All 8 phase-wise documents required for submission are in [`/docs`](./docs):
1. `01-Brainstorming-Ideation-Phase.md`
2. `02-Requirement-Analysis-Phase.md`
3. `03-Project-Design-Phase.md`
4. `04-Project-Planning-Phase.md`
5. `05-Project-Development-Phase.md`
6. `06-Project-Testing-Phase.md`
7. `07-Project-Documentation-Phase.md`
8. `08-Project-Demonstration-Phase.md`

## Folder Structure
```
LegalEase/
├── ai_core/
│   └── gemini_generator.py      # Gemini prompt + API call
├── docs/                        # 8 phase-wise submission documents
├── frontend/
│   └── app.py                   # Streamlit UI
├── Image/
│   ├── Logo.png
│   └── inverseLogo.png
├── legalEaseAPI/
│   ├── main.py                  # FastAPI app entry point
│   └── routes.py                # /generate endpoint
├── utils/
│   └── formatting.py            # sanitize_text, format_docx, format_pdf, format_html_preview
├── .env.example
├── config.py
├── requirements.txt
├── run.sh
└── README.md
```

## Setup

1. **Clone the repo and create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # then edit .env and paste your Gemini API key
   ```
   Get a key from [Google AI Studio](https://aistudio.google.com/app/apikey).

4. **Run the backend** (in one terminal)
   ```bash
   uvicorn legalEaseAPI.main:app --reload --port 8000
   ```

5. **Run the frontend** (in a second terminal)
   ```bash
   streamlit run frontend/app.py
   ```

   Or run both together:
   ```bash
   bash run.sh
   ```

6. Open the app at `http://localhost:8501`.

## Usage
1. Enter **Document Type** (e.g., `Freelance Work Contract`), **Parties Involved**, **Terms & Conditions** (semicolon-separated), and **Effective Date**.
2. Click **Generate Document**.
3. Preview, optionally click **Click to Edit Document** to revise.
4. Download as **.TXT**, **.DOCX**, or **.PDF** — both exports include the LegalEase logo and footer.

## Notes
- This tool produces AI-generated drafts; have a qualified professional review any document before formal use.
- Replace `Image/Logo.png` and `Image/inverseLogo.png` with your own branding if needed.
