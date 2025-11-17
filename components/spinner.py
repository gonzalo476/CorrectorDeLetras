from qtpy import QtWidgets, QtCore, QtGui
import os


class SpinnerDialog(QtWidgets.QDialog):

    def __init__(self, message: str = "Cargando...", parent=None):
        super().__init__(parent)

        # === RUTA ABSOLUTA DEL GIF ===
        BASE = os.path.dirname(os.path.abspath(__file__))
        self.gif_path = os.path.join(BASE, "..", "resources", "gif", "Loading.gif")
        self.gif_path = os.path.abspath(self.gif_path)

        print("GIF path final:", self.gif_path)

        # === CONFIG VENTANA ===
        self.setWindowTitle("Por favor espera…")
        self.setModal(False)
        self.setWindowFlags(
            QtCore.Qt.Dialog
            | QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)

        # === GIF ===
        self.spinner_label = QtWidgets.QLabel()

        self.movie = QtGui.QMovie(self.gif_path)
        self.spinner_label.setScaledContents(True)
        self.spinner_label.setFixedSize(50, 50)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)

        self.spinner_label.setMovie(self.movie)
        self.spinner_label.setAlignment(QtCore.Qt.AlignCenter)

        print("GIF isValid:", self.movie.isValid())

        # === TEXTO ===
        self.message_label = QtWidgets.QLabel(message)
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        font = self.message_label.font()
        font.setPointSize(12)
        self.message_label.setFont(font)

        # Añadir al layout
        layout.addWidget(self.spinner_label)
        layout.addWidget(self.message_label)
        self.setLayout(layout)

        self.setFixedSize(250, 200)

    # ==========================================================
    #              CENTRAR EN PANTALLA
    # ==========================================================
    def center_on_screen(self):
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        dlg = self.frameGeometry()
        x = (screen.width() - dlg.width()) // 2
        y = (screen.height() - dlg.height()) // 2
        self.move(x, y)

    # ==========================================================
    #              MOSTRAR / OCULTAR SPINNER
    # ==========================================================
    def show_spinner(self):
        self.adjustSize()
        self.center_on_screen()
        self.movie.start()
        self.show()
        QtWidgets.QApplication.processEvents()

    def hide_spinner(self):
        self.movie.stop()
        self.hide()

    def set_message(self, message: str):
        self.message_label.setText(message)
