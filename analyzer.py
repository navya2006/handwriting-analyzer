import os
import json
import mimetypes

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

PROMPT = """
You are an expert handwriting analyst.

Analyze the uploaded handwritten document.

Return ONLY valid JSON in the following format.

{
    "overall_score": 0,
    "legibility": 0,
    "letter_consistency": 0,
    "word_spacing": 0,
    "line_spacing": 0,
    "baseline_alignment": 0,
    "margin_consistency": 0,
    "slant": "",
    "writing_style": "",
    "estimated_level": "",
    "strengths": [],
    "weaknesses": [],
    "improvements": [],
    "difficult_words": [],
    "extracted_text": ""
}

Rules:
- Scores must be between 0 and 100.
- extracted_text must preserve formatting as much as possible.
- Return ONLY JSON.
"""


def _clean_json(text: str):
    """
    Removes ```json ... ``` wrappers if Gemini adds them.
    """

    text = text.strip()

    if text.startswith("```json"):
        text = text[7:]

    if text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def analyze_handwriting(file_path: str):

    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type is None:
        raise ValueError("Unsupported file type.")

    with open(file_path, "rb") as f:
        file_bytes = f.read()

    response = client.models.generate_content(
        model="models/gemini-flash-latest",  
        contents=[
            PROMPT,
            types.Part.from_bytes(
                data=file_bytes,
                mime_type=mime_type,
            ),
        ],
    )

    text = _clean_json(response.text)

    try:
        return json.loads(text)

    except json.JSONDecodeError:

        return {
            "overall_score": 0,
            "legibility": 0,
            "letter_consistency": 0,
            "word_spacing": 0,
            "line_spacing": 0,
            "baseline_alignment": 0,
            "margin_consistency": 0,
            "slant": "",
            "writing_style": "",
            "estimated_level": "",
            "strengths": [],
            "weaknesses": [],
            "improvements": [],
            "difficult_words": [],
            "extracted_text": "",
            "raw_response": response.text
        }