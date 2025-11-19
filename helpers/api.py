from google import genai
from google.genai import types


def test_api_key(api_key: str) -> bool:
    try:
        client = genai.Client(api_key=api_key)

        client.models.generate_content(
            model="gemini-2.0-flash",
            contents="ping",
            config=types.GenerateContentConfig(max_output_tokens=1, temperature=0.0),
        )
        return True

    except Exception:
        return False
