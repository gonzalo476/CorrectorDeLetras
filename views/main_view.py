from qtpy import QtWidgets, QtGui

from controllers.main_controller import SongCorrectionController

from components.button import Button
from components.dialog import InfoMessage, SuccessMessage

from helpers.icon import IconHelper
from helpers.copy import format_propresenter_text

from controllers.service_controller import ServiceController
from config.colors import UIColors


class MainView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.window_icon = IconHelper.get_window_icon_path()
        self.correct_song = SongCorrectionController(view=self)

        # services
        self.services = ServiceController()

        # window configs
        self.setWindowTitle("Corrector de letras")
        self.setMinimumSize(700, 600)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QtGui.QColor(UIColors.BG_DARK))
        self.setPalette(palette)
        self.setWindowIcon(QtGui.QIcon(str(self.window_icon)))

        # main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        self.setLayout(main_layout)

        # actions button layout
        button_actions_layout = QtWidgets.QHBoxLayout()

        # editor layout
        editor_layout = QtWidgets.QHBoxLayout()

        # options tools layout
        tools_layout = QtWidgets.QHBoxLayout()

        # copy layout
        copy_layout = QtWidgets.QHBoxLayout()

        # checkbox uppercase
        self.set_uppercase_box = QtWidgets.QCheckBox()
        self.set_uppercase_box.setObjectName("set_uppercase_box")
        self.set_uppercase_box.setText("Mayúscula")
        self.set_uppercase_box.setChecked(True)

        # checkbox divide
        self.set_divide_box = QtWidgets.QCheckBox()
        self.set_divide_box.setObjectName("set_divide_box")
        self.set_divide_box.setText("Dividir En Secciones")
        self.set_divide_box.setChecked(True)

        # checkbox repeated words
        self.set_reduce_box = QtWidgets.QCheckBox()
        self.set_reduce_box.setObjectName("set_reduce_box")
        self.set_reduce_box.setText("Reducir")
        self.set_reduce_box.setChecked(True)

        # original
        self.original_txt = QtWidgets.QTextEdit()
        self.original_txt.setObjectName("original_txt")
        self.original_txt.setPlaceholderText("Pega el texto de la cancion aquí..")
        self.original_txt.setStyleSheet(
            """
            QTextEdit {
                background-color: #212426;
                color: white;                        
            }
        """
        )

        # corrected
        self.corrected_txt = QtWidgets.QTextEdit()
        self.corrected_txt.setObjectName("corrected_txt")
        self.corrected_txt.setPlaceholderText("")
        self.corrected_txt.setStyleSheet(
            """
            QTextEdit {
                background-color: #212426;
                color: white;                        
            }
        """
        )

        # button
        self.icon_helper = IconHelper()
        self.delete_btn = Button(text="Eliminar", variant="danger")
        self.correct_btn = Button(text="Corregir")
        self.copy_corrected_btn = Button(
            text="Copiar Letra Corregida",
            type="text",
            variant="secondary",
            icon=self.icon_helper.get_icon(icon="copy.png"),
        )
        self.copy_to_propresenter_btn = Button(
            text="Copiar para ProPresenter",
            type="text",
            variant="secondary",
            icon=self.icon_helper.get_icon(icon="propresenter.png"),
        )

        # actions button layout
        button_actions_layout.addWidget(self.delete_btn)
        button_actions_layout.addWidget(self.correct_btn)

        # connects
        self.copy_corrected_btn.clicked.connect(self.handle_copy)
        self.correct_btn.clicked.connect(self.handle_correct)
        self.delete_btn.clicked.connect(self.handle_delete)
        self.copy_to_propresenter_btn.clicked.connect(self.handle_copy_to_propresenter)

        # tools layout
        tools_layout.addStretch()
        tools_layout.addWidget(self.set_uppercase_box)
        tools_layout.addWidget(self.set_reduce_box)
        tools_layout.addWidget(self.set_divide_box)
        tools_layout.addStretch()

        # editor layout
        editor_layout.addWidget(self.original_txt)
        editor_layout.addWidget(self.corrected_txt)

        # copy layout
        copy_layout.addWidget(self.copy_corrected_btn)
        copy_layout.addWidget(self.copy_to_propresenter_btn)

        # main layout
        main_layout.addLayout(tools_layout)
        main_layout.addLayout(editor_layout)
        main_layout.addLayout(button_actions_layout)
        main_layout.addLayout(copy_layout)

    def handle_copy(self):
        clipboard = QtWidgets.QApplication.clipboard()
        text = self.corrected_txt.toPlainText()

        if not text:
            InfoMessage(msg="Ingresa una cancion para copiar").exec()
            return
        clipboard.setText(text)
        SuccessMessage(msg="Texto copiado al portapapeles correctamente").exec()

    def handle_copy_to_propresenter(self):
        clipboard = QtWidgets.QApplication.clipboard()
        text = self.corrected_txt.toPlainText()

        text_to_copy = format_propresenter_text(text=text)

        if not text:
            InfoMessage(msg="Ingresa una cancion para copiar").exec()
            return
        clipboard.setText(text_to_copy)
        SuccessMessage(msg="Texto copiado al portapapeles correctamente").exec()

    def handle_delete(self):
        self.original_txt.setText("")
        self.corrected_txt.setText("")

    def handle_correct(self):
        self.corrected_txt.setText("")

        self.services.validate_key()

        text = self.original_txt.toPlainText()
        divide = self.set_divide_box.isChecked()
        reduce = self.set_reduce_box.isChecked()
        uppercase = self.set_uppercase_box.isChecked()

        self.correct_song.correct_song(
            text, divide=divide, reduce=reduce, uppercase=uppercase
        )

    def show_corrected_text(self, text: str):
        self.corrected_txt.setText(text)
