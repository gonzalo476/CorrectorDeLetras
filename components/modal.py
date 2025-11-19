from qtpy import QtWidgets
from components.button import Button


class APIKeyModal(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_key = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Configurar API Key")
        self.setModal(True)
        self.setGeometry(100, 100, 400, 150)

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        layout.addWidget(QtWidgets.QLabel("Key:"))

        self.input = QtWidgets.QLineEdit()
        self.input.setFixedHeight(30)
        self.input.setPlaceholderText("sk-...")
        layout.addWidget(self.input)

        btn_layout = QtWidgets.QHBoxLayout()

        btn_cancel = Button(text="Cancelar", variant="danger")
        btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(btn_cancel)

        btn_save = Button(text="Guardar", variant="primary")
        btn_save.clicked.connect(self.save)
        btn_layout.addWidget(btn_save)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def save(self):
        self.api_key = self.input.text().strip()
        if self.api_key:
            self.accept()
        else:
            self.input.setStyleSheet("border: 1px solid red;")

    def get_api_key(self):
        return self.api_key
