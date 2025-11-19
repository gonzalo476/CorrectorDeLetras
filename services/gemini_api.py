from google import genai
from models.response import Response

from services.settings_service import SettingsService


class SongCorrectionService:
    def __init__(self):
        self.settings = SettingsService()
        self.api_key = self.settings.load_api_key()
        self.client = genai.Client(api_key=self.api_key)

    def correct(
        self, text: str, divide: bool, reduce: bool, uppercase: bool
    ) -> Response:

        divide_prompt = "Identifica y Divide la letra usando las siguientes secciones musicales: //INTRO, //VERSO, //PRE-CORO, //CORO, //POST-CORO, //PUENTE, //SPONTANEO, //OUTRO"
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
                model="gemini-flash-latest", contents=prompt
            )
            data = response.text.upper() if uppercase == True else response.text
            return Response(True, data)
        except Exception as e:
            return Response(False, error=f"Error: {str(e)}")
