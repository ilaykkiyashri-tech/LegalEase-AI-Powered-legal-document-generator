# Phase 4: Project Planning

## Milestone Plan

| Milestone | Focus | Key Activities |
|-----------|-------|-----------------|
| M1 | Model Selection & Architecture | Select Gemini 1.5 Pro; define frontend/backend/AI-core architecture; set up dev environment (.env, API key) |
| M2 | Core Functionalities Development | Legal document generation logic; DOCX/PDF/HTML formatting functions; Streamlit input handling; editable preview & downloads |
| M3 | API Logic Integration | Build `main.py` (FastAPI app, root endpoint, router); build `routes.py` (Pydantic model, `/generate` endpoint, Gemini call) |
| M4 | Frontend Development | Streamlit page config & layout; header/logo; input interface; dynamic preview and multi-format export |
| M5 | Deployment | Set up virtual environment; install dependencies from `requirements.txt`; configure `.env`; launch FastAPI (Uvicorn) and Streamlit locally; end-to-end testing |

## Suggested Timeline (adjust to your team's actual schedule)
- **Week 1:** Milestone 1 — architecture & environment setup
- **Week 2:** Milestone 2 — core generation & formatting logic
- **Week 3:** Milestone 3 — API integration
- **Week 4:** Milestone 4 — frontend build-out
- **Week 5:** Milestone 5 — local deployment, testing, documentation, and demo recording
## Team Members

| Name | Role |
|------|------|
| Desika | Team Member |
| Ilakkia Shri | Team Member |
| Miracle Iniya | Team Member |
| Divya Sree | Team Member |
| Jayalakshmisri | Team Member |

## Risk & Dependency Notes
- Gemini API key must be obtained and stored securely in `.env` before M1 can be tested end-to-end.
- Formatting modules (M2) depend on finalized AI output structure from M1.
- Frontend (M4) depends on a working `/generate` endpoint (M3).
- Deployment testing (M5) depends on all prior milestones being functionally complete.

## Deliverables Checklist per GitHub Submission Structure
1. Brainstorming & Ideation Phase — done
2. Requirement Analysis Phase — done
3. Project Design Phase — done
4. Project Planning Phase — done (this document)
5. Project Development Phase — source code + notes
6. Project Testing Phase — test cases & results
7. Project Documentation Phase — README, user guide, API docs
8. Project Demonstration Phase — demo video script + link
