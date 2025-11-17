from qtpy import QtWidgets

from controllers.main_controller import SongCorrectionController
from components.button import Button


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Corrector De Letras")
        self.setMinimumSize(500, 600)

        # main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        # editor layout
        editor_layout = QtWidgets.QHBoxLayout()

        # options tools layout
        tools_layout = QtWidgets.QHBoxLayout()

        # checkbox options
        self.set_uppercase_box = QtWidgets.QCheckBox()
        self.set_uppercase_box.setText("Mayúscula")
        self.set_uppercase_box.setChecked(True)

        # original
        self.original_txt = QtWidgets.QTextEdit()
        self.original_txt.setObjectName("original_txt")
        self.original_txt.setPlaceholderText("Pega el texto de la cancion aquí..")

        # corrected
        self.corrected_txt = QtWidgets.QTextEdit()
        self.corrected_txt.setObjectName("corrected_txt")
        self.corrected_txt.setPlaceholderText("")

        # button
        self.correct_btn = Button(text="Corregir")
        self.copy_corrected_btn = Button(
            text="Copiar Letra Corregida", type="text", variant="secondary"
        )

        # connects
        self.copy_corrected_btn.clicked.connect(self.handle_copy)
        self.correct_btn.clicked.connect(self.handle_correct)

        # tools layout
        tools_layout.addStretch()
        tools_layout.addWidget(self.set_uppercase_box)
        tools_layout.addStretch()

        # editor layout
        editor_layout.addWidget(self.original_txt)
        editor_layout.addWidget(self.corrected_txt)

        # main layout
        main_layout.addLayout(tools_layout)
        main_layout.addLayout(editor_layout)
        main_layout.addWidget(self.correct_btn)
        main_layout.addWidget(self.copy_corrected_btn)

    def handle_copy(self):
        print("text copied..")

    def handle_correct(self):
        self.correct_song = SongCorrectionController()
        self.corrected_txt.setText("")
        text = self.original_txt.toPlainText()
        corrected_song = self.correct_song.correct_song(text)
        self.corrected_txt.setText(corrected_song)
