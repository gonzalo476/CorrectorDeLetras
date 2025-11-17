from google import genai
from models.response import Response

API_KEY = "AIzaSyB8599YPiFTE6ErbGNJP_1Yj-Y0tpujW7U"


class SongCorrectionService:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def correct(self, text: str) -> Response:
        prompt = f"""Eres un corrector de letras de canciones en español.
        Corrige ÚNICAMENTE acentos y ortografía.
        Devuelve solo el texto corregido, sin explicaciones.

        Texto:
        {text}
        """

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
            return Response(True, data=response.text)
        except Exception as e:
            return Response(False, error=f"Error: {str(e)}")
