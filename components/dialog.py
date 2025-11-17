from PySide6 import QtWidgets, QtGui, QtCore


class WarningMessage(QtWidgets.QDialog):

    def __init__(self, msg="message", title="Warning", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.btn_box = QtWidgets.QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        icon_label = QtWidgets.QLabel()
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxWarning)
        icon_label.setPixmap(icon.pixmap(48, 48))

        message = QtWidgets.QLabel(msg)
        message.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        layout.addWidget(icon_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(message, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)


class InfoMessage(QtWidgets.QDialog):

    def __init__(self, msg="message", title="Info", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.btn_box = QtWidgets.QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        icon_label = QtWidgets.QLabel()
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxInformation)
        icon_label.setPixmap(icon.pixmap(48, 48))

        message = QtWidgets.QLabel(msg)
        message.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        layout.addWidget(icon_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(message, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)


class CriticalMessage(QtWidgets.QDialog):

    def __init__(self, msg="message", title="Critical", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.btn_box = QtWidgets.QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        icon_label = QtWidgets.QLabel()
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxCritical)
        icon_label.setPixmap(icon.pixmap(48, 48))

        message = QtWidgets.QLabel(msg)
        message.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        layout.addWidget(icon_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(message, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)


class QuestionMessage(QtWidgets.QDialog):

    def __init__(self, msg="message", title="Question", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        self.btn_box = QtWidgets.QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)
        self.btn_box.rejected.connect(self.reject)

        icon_label = QtWidgets.QLabel()
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxQuestion)
        icon_label.setPixmap(icon.pixmap(48, 48))

        message = QtWidgets.QLabel(msg)
        message.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        layout.addWidget(icon_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(message, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)


class SuccessMessage(QtWidgets.QDialog):

    def __init__(self, msg="message", title="Success", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)

        QBtn = QtWidgets.QDialogButtonBox.Ok
        self.btn_box = QtWidgets.QDialogButtonBox(QBtn)
        self.btn_box.accepted.connect(self.accept)

        icon_label = QtWidgets.QLabel()
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_DialogApplyButton)
        icon_label.setPixmap(icon.pixmap(48, 48))

        message = QtWidgets.QLabel(msg)
        message.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(msg)
        layout.addWidget(icon_label, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(message, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.btn_box)
        self.setLayout(layout)
