# Phase 8: Project Demonstration

## Demo Video Requirements (per submission guidelines)
- Screen sharing of the running project
- Student's voice-over/explanation throughout
- Must cover: Project Name, Purpose, Use/Benefits, Execution/Working Process, and Final Output
- Uploaded to Google Drive with link set to "Anyone with the link can view"

## Suggested Demo Script / Outline

### 1. Introduction (0:00–0:30)
- "Hi, I'm [name], and this is **LegalEase** — an AI-powered legal document generator."
- One-line purpose: "It helps entrepreneurs, freelancers, and individuals generate professional legal documents like contracts, NDAs, and lease agreements without needing a legal background."

### 2. Purpose & Benefits (0:30–1:15)
- Problem: drafting legal documents is costly/inaccessible without legal expertise.
- Benefit: LegalEase uses Google's Gemini AI to generate structured, professional documents from a few simple inputs, with editable previews and export in TXT, DOCX, and PDF.

### 3. Architecture Walkthrough (1:15–2:00)
- Briefly show the diagram: Streamlit frontend → FastAPI backend → Gemini AI core → formatted output.
- Mention the tech stack: FastAPI, Streamlit, Gemini 1.5 Pro, python-docx, FPDF.

### 4. Live Execution / Working Process (2:00–4:30)
- Show the running app at `localhost:8501`.
- Fill in the four fields (use a sample: Freelance Work Contract, parties, terms, date).
- Click **Generate Document** — show the AI-generated preview.
- Click **Click to Edit Document** and make a small edit.
- Download and open the **.TXT** file.
- Download and open the **.DOCX** file — point out the logo and footer.
- Download and open the **.PDF** file — point out the branded header/footer on every page.

### 5. Final Output & Wrap-up (4:30–5:00)
- Recap: a complete, branded, ready-to-use legal document generated in seconds.
- Mention future enhancements (cloud deployment, multilingual support).
- Thank the viewer.

## Checklist Before Recording
- [ ] Backend (`uvicorn`) and frontend (`streamlit`) both running without errors
- [ ] `.env` configured with a working `GEMINI_API_KEY`
- [ ] Sample inputs prepared in advance (document type, parties, terms, date)
- [ ] Screen recording software ready (e.g., OBS, Loom)
- [ ] Microphone tested for clear voice-over
- [ ] Video uploaded to Google Drive with sharing set to "Anyone with the link can view"
- [ ] Link added to the GitHub repository README and final submission
