import sys
from pathlib import Path
from qtpy.QtGui import QIcon


class IconHelper:

    @staticmethod
    def get_window_icon_path() -> Path:
        icon_name = "AppIcon.icns" if sys.platform == "darwin" else "AppIcon.ico"
        return Path(__file__).parent.parent / "resources" / "icons" / icon_name

    @staticmethod
    def get_icon(icon: str) -> QIcon:
        icon_path = Path(__file__).parent.parent / "resources" / "icons" / icon
        return QIcon(str(icon_path))
