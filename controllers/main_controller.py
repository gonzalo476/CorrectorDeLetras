from services.gemini_api import SongCorrectionService
from components.dialog import WarningMessage, InfoMessage


class SongCorrectionController:
    def __init__(self):
        self.service = SongCorrectionService()

    def correct_song(self, text: str):

        if not text:
            InfoMessage(msg="Por favor introduce el texto de la canción.").exec()
            return

        corrected = self.service.correct(text)

        if not corrected.success:
            WarningMessage(msg=corrected.error)
            return

        return corrected.data
