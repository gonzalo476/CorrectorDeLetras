from qtpy.QtCore import QThread, QObject, Signal
from workers.worker import Worker
from services.gemini_api import SongCorrectionService
from components.dialog import WarningMessage, InfoMessage


class SongCorrectionController(QObject):
    finished = Signal(str)

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.service = SongCorrectionService()

    def correct_song(self, text: str, divide: bool, reduce: bool, uppercase: bool):

        if not text:
            InfoMessage(msg="Por favor introduce el texto de la canción.").exec()
            return

        # Activar spinner en el botón
        self.view.correct_btn.set_loading(True, spinner_size=16)

        # Thread + Worker
        self.thread = QThread()
        self.worker = Worker(self.service, text, divide, reduce, uppercase)
        self.worker.moveToThread(self.thread)

        # Conexiones
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self._on_correct_finished)
        self.worker.error.connect(self._on_correct_error)

        # Cerrar hilo
        self.worker.finished.connect(self.thread.quit)
        self.worker.error.connect(self.thread.quit)

        self.thread.start()

    def _on_correct_finished(self, response):
        # Desactivar spinner
        self.view.correct_btn.set_loading(False)

        # Mostrar resultado
        self.view.show_corrected_text(response.data)

    def _on_correct_error(self, error):
        # Desactivar spinner
        self.view.correct_btn.set_loading(False)

        WarningMessage(msg=error).exec()
