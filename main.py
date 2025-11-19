import sys
from qtpy import QtWidgets

from controllers.service_controller import ServiceController

from views.main_view import MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    service = ServiceController()

    if not service.request_api_key():
        sys.exit(0)

    window = MainView()
    window.show()

    app.exec()
