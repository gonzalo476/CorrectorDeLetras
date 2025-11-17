import sys
from qtpy import QtWidgets

from views.main_view import MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainView()
    window.show()

    app.exec()
