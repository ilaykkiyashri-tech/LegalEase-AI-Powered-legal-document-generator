# Phase 2: Requirement Analysis

## Functional Requirements
| ID | Requirement |
|----|-------------|
| FR1 | User can select/enter a document type (e.g., Agreement, Contract, NDA, Lease Agreement, Employment Offer Letter) |
| FR2 | User can enter parties involved (names and roles) |
| FR3 | User can enter terms & conditions as semicolon-separated clauses |
| FR4 | User can enter an effective date |
| FR5 | System generates a structured legal document via Gemini AI based on the above inputs |
| FR6 | User can preview the generated document as styled HTML |
| FR7 | User can edit the generated document inline before export |
| FR8 | User can download the document as .TXT, .DOCX, or .PDF |
| FR9 | Exported DOCX/PDF include company logo, consistent fonts, and a terms table/footer |

## Non-Functional Requirements
- **Usability:** Simple, guided Streamlit interface requiring no legal knowledge
- **Performance:** Document generation should complete within a few seconds per request
- **Security:** Sensitive user data (names, terms, dates) handled securely; API keys stored in `.env`, not hardcoded
- **Reliability:** Consistent formatting across all three export formats
- **Portability:** Runs locally first (Milestone 5), with a clear path to cloud deployment

## Technical Requirements / Pre-requisites
- FastAPI framework knowledge
- Google Gemini API familiarity (Generative AI SDK)
- Streamlit for frontend development
- Python 3.10+ proficiency
- Environment setup: `pip install fastapi uvicorn streamlit python-docx fpdf Pillow requests google-generativeai python-dotenv`

## Stakeholders
- **End users:** startup founders, freelancers, landlords, individuals
- **Development team:** builds and maintains backend, frontend, and AI integration
- **Faculty/evaluators (Smartbridge / Smart Internz):** review phase-wise submissions and final demo

## Inputs & Data Model
`DocumentRequest` (Pydantic model):
- `document_type: str`
- `parties: str`
- `terms: str`
- `dates: str`

## Out of Scope (for this project phase)
- Legal validity review by a licensed attorney
- E-signature integration
- Multi-language document generation (noted as a future enhancement)
