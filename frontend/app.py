import os
import sys

import requests
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.formatting import format_docx, format_html_preview, format_pdf, sanitize_text  # noqa: E402

st.set_page_config(page_title="LegalEase", layout="centered")

LOGO_PATH = os.getenv("LOGO_PATH", "Image/Logo.png")
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, use_container_width=True)
    else:
        st.markdown("<h1 style='text-align:center;'>LegalEase</h1>", unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align: center;'>AI Legal Document Generator</h2>",
    unsafe_allow_html=True,
)

document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

if st.button("Generate Document"):
    if not document_type or not parties:
        st.warning("Please fill in at least the Document Type and Parties Involved.")
    else:
        try:
            response = requests.post(
                f"{BACKEND_URL}/generate",
                json={
                    "document_type": document_type,
                    "parties": parties,
                    "terms": terms,
                    "dates": dates,
                },
                timeout=60,
            )
            response.raise_for_status()
            st.session_state.generated_text = sanitize_text(response.json()["document"])
            st.session_state.show_edit = False
            st.success("Document Generated Successfully!")
        except requests.exceptions.RequestException as exc:
            st.error(f"Could not reach the LegalEase backend: {exc}")
        except Exception as exc:  # noqa: BLE001
            st.error(f"Generation failed: {exc}")

if st.session_state.generated_text:
    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(
        "<div style='background:#111318;padding:16px;border-radius:10px;"
        "max-height:420px;overflow-y:auto;border:1px solid #2a2d35;'>"
        f"{styled_html}</div>",
        unsafe_allow_html=True,
    )

    if st.button("Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit

    if st.session_state.show_edit:
        edited_text = st.text_area(
            "Edit Document Below:",
            st.session_state.generated_text,
            height=300,
        )
        st.session_state.generated_text = edited_text

    safe_name = (document_type or "legal_document").strip().replace(" ", "_").lower()

    dcol1, dcol2, dcol3 = st.columns(3)
    with dcol1:
        st.download_button(
            "Download as .TXT",
            data=st.session_state.generated_text,
            file_name=f"{safe_name}.txt",
        )
    with dcol2:
        st.download_button(
            "Download as .DOCX",
            data=format_docx(st.session_state.generated_text, document_type, parties, terms, dates),
            file_name=f"{safe_name}.docx",
        )
    with dcol3:
        st.download_button(
            "Download as .PDF",
            data=format_pdf(st.session_state.generated_text, document_type, terms),
            file_name=f"{safe_name}.pdf",
        )
else:
    st.info("Click 'Generate Document' to start")
