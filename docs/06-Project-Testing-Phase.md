# Phase 6: Project Testing

## Test Environment
- Backend running via `uvicorn legalEaseAPI.main:app --reload` on `http://127.0.0.1:8000`
- Frontend running via `streamlit run frontend/app.py` on `http://localhost:8501`

## Test Categories

### 1. Backend / API Testing
| Test Case | Input | Expected Result |
|-----------|-------|------------------|
| TC-01 | Valid `document_type`, `parties`, `terms`, `dates` | Returns 200 with generated document text |
| TC-02 | Missing a required field | Returns 422 validation error (Pydantic) |
| TC-03 | Empty `terms` field | Document generated without a terms table/bullets, no crash |
| TC-04 | Very long `terms` input | Document generated without truncation errors |
| TC-05 | Special characters in inputs (quotes, emojis) | `sanitize_text` cleans output correctly |

### 2. Document Type Coverage
Test generation for each supported type:
- Employment Contract
- NDA (Non-Disclosure Agreement)
- Lease Agreement
- Freelance/Service Contract
- Employment Offer Letter

### 3. Export Format Testing
| Format | Checks |
|--------|--------|
| .TXT | Plain text downloads correctly, content matches preview |
| .DOCX | Logo appears on first page, Times New Roman formatting, terms rendered as a table, footer on last page |
| .PDF | Logo and footer appear on every page, headings bold, terms as bullet points |

### 4. Frontend / UX Testing
- Input fields accept and retain text correctly
- "Generate Document" triggers a POST request and displays a success message
- HTML preview renders correctly in dark mode
- "Click to Edit Document" opens an editable text area pre-filled with generated content
- Edits made in the text area are reflected in all three download formats

### 5. Integration / End-to-End Testing (per Milestone 5, Activity 5.2)
1. Input document type, parties, terms, and date
2. Click "Generate Document" → verify AI-generated content appears
3. Preview in dark-mode HTML
4. Edit the text
5. Download in .txt, .docx, and .pdf formats
6. Verify: proper layout with logo and footer, clean bullet formatting, correct embedding of terms

## Bug Tracking Template
| ID | Description | Severity | Status | Fixed In |
|----|--------------|----------|--------|----------|
| BUG-01 | example | Low/Med/High | Open/Closed | commit/PR # |

## Sign-off Criteria
- All test cases above pass with no unhandled exceptions
- Generated documents are legible, correctly formatted, and consistent across all three export formats
