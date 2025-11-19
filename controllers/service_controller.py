from qtpy import QtWidgets

from services.settings_service import SettingsService
from components.modal import APIKeyModal
from components.dialog import WarningMessage, SuccessMessage, InfoMessage

from helpers.api import test_api_key


class ServiceController:
    def __init__(self):
        self.settings = SettingsService()
        self.api_key = self.settings.load_api_key()
        self.modal = None

    def request_api_key(self):
        if self.api_key:
            return True

        while True:
            self.modal = APIKeyModal()

            if self.modal.exec() != QtWidgets.QDialog.Accepted:
                return False

            api_key_input = self.modal.get_api_key()

            if test_api_key(api_key=api_key_input):
                self.settings.save_api_key(key=api_key_input)
                SuccessMessage(msg="API Key válida").exec()
                return True
            else:
                WarningMessage(msg="API Key inválida").exec()

    def validate_key(self):
        if not test_api_key(api_key=self.api_key):

            InfoMessage(
                msg="Tu API Key dejó de ser válida. Por favor ingresa una nueva."
            ).exec()

            while True:
                self.modal = APIKeyModal()

                if self.modal.exec() != QtWidgets.QDialog.Accepted:
                    return False

                api_key_input = self.modal.get_api_key()

                if test_api_key(api_key=api_key_input):
                    self.settings.save_api_key(key=api_key_input)
                    SuccessMessage(msg="API Key válida").exec()
                    return True
                else:
                    WarningMessage(msg="API Key inválida").exec()
