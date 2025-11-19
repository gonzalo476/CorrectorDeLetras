import keyring


class SettingsService:
    SERVICE_NAME = "corrector_de_letras"
    USERNAME = "GENAI_API_KEY"

    def save_api_key(self, key: str):
        keyring.set_password(self.SERVICE_NAME, self.USERNAME, key)

    def load_api_key(self) -> str:
        return keyring.get_password(self.SERVICE_NAME, self.USERNAME)

    def delete_api_key(self):
        keyring.delete_password(self.SERVICE_NAME, self.USERNAME)
