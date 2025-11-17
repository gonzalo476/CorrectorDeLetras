from google import genai
from models.response import Response

API_KEY = "AIzaSyB8599YPiFTE6ErbGNJP_1Yj-Y0tpujW7U"


class SongCorrectionService:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def correct(
        self, text: str, divide: bool, reduce: bool, uppercase: bool
    ) -> Response:

        divide_prompt = "Divide la letra en secciones musicales típicas así: //VERSO, //CORO, //PUENTE, etc."
        reduce_prompt = "Analiza y elimina lineas extra que se repiten con frecuencia ya sea el verso, coro o puente."

        prompt = f"""
        Eres un analizador profesional de letras de canciones en español.

        Reglas:
        - NO modifiques ninguna palabra del texto.
        - NO inventes contenido.
        - NO uses formato Markdown.
        - NO uses comillas ni backticks.
        - {divide_prompt if divide == True else ""}
        - {reduce_prompt if reduce == True else ""}
        - Devuelve solo el texto sin explicaciones adicionales.

        Texto:
        {text}
        """

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
            data = response.text.upper() if uppercase == True else response.text
            return Response(True, data)
        except Exception as e:
            return Response(False, error=f"Error: {str(e)}")
