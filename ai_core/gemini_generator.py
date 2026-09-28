import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY", ""))


class GeminiDocumentGenerator:
    """Wraps the Gemini model and turns structured user input into a
    formal legal document draft."""

    def __init__(self, model_name: str = "gemini-flash-latest"):
        self.model = genai.GenerativeModel(model_name)

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            "Ensure a formal legal structure with clearly numbered sections and "
            "standard legal clauses (definitions, obligations, term/termination, "
            "confidentiality if relevant, governing law, signature block). "
            "Do not wrap the output in markdown code fences."
        )
        response = self.model.generate_content(prompt)
        return response.text
