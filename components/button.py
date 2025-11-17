from qtpy import QtWidgets, QtCore, QtGui
from typing import Literal, Optional, Union
import os
from config.colors import AppleColors


class Button(QtWidgets.QPushButton):
    def __init__(
        self,
        text: str = "Button",
        variant: Literal["primary", "success", "danger", "secondary"] = "primary",
        type: Literal["filled", "text"] = "filled",
        size: Literal["small", "medium", "large"] = "small",
        full_width: bool = False,
        icon: Optional[Union[QtGui.QIcon, str]] = None,
        icon_size: Optional[QtCore.QSize] = None,
        parent: Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(text, parent)

        self.variant = variant
        self.size = size
        self.full_width = full_width
        self.type = type

        self._loading = False
        self._saved_icon = None
        self._saved_text = text
        self._loading_movie = None

        if icon is not None:
            self._set_icon(icon, icon_size)

        self._set_style()
        self._set_size()

    def set_loading(
        self, value: bool, spinner_path: str = None, spinner_size: int = 16
    ):
        if spinner_path is None:
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            spinner_path = os.path.join(project_root, "resources", "gif", "spin.gif")

        if value and not self._loading:
            self._loading = True
            self._saved_text = self.text()
            self._saved_icon = self.icon()

            self.setText("")
            self.setIconSize(QtCore.QSize(spinner_size, spinner_size))

            self._loading_movie = QtGui.QMovie(spinner_path)
            if self._loading_movie.isValid():
                self._loading_movie.frameChanged.connect(self._update_spinner_frame)
                self._loading_movie.start()
                # Forzar el primer frame
                self._update_spinner_frame()
            else:
                print(f"Error: No se pudo cargar el GIF en: {spinner_path}")
                print(
                    f"Verificar que el archivo exista en: {os.path.abspath(spinner_path)}"
                )
            self.blockSignals(True)

        elif not value and self._loading:
            self._loading = False

            if self._loading_movie:
                try:
                    self._loading_movie.frameChanged.disconnect(
                        self._update_spinner_frame
                    )
                except RuntimeError:
                    pass
                self._loading_movie.stop()
                self._loading_movie = None

            self.setIcon(self._saved_icon if self._saved_icon else QtGui.QIcon())
            self.setText(self._saved_text)

            self.blockSignals(False)

    def _update_spinner_frame(self):
        """Actualiza el icono del botón con el frame actual del GIF."""
        if not self._loading or not self._loading_movie:
            return
        pixmap = self._loading_movie.currentPixmap()
        if not pixmap.isNull():
            self.setIcon(QtGui.QIcon(pixmap))

    def _set_icon(
        self, icon: Union[QtGui.QIcon, str], icon_size: Optional[QtCore.QSize] = None
    ):
        if isinstance(icon, str):
            q_icon = QtGui.QIcon(icon)
        else:
            q_icon = icon

        self.setIcon(q_icon)

        if icon_size is None:
            sizes_map = {"small": 16, "medium": 20, "large": 24}
            icon_pixel_size = sizes_map.get(self.size, 20)
            icon_size = QtCore.QSize(icon_pixel_size, icon_pixel_size)

        self.setIconSize(icon_size)

    def _set_style(self):
        colors = {
            "primary": {
                "normal": AppleColors.BLUE,
                "hover": AppleColors.BLUE_HOVER,
                "pressed": AppleColors.BLUE_PRESSED,
                "disabled": AppleColors.BLUE_DISABLED,
            },
            "success": {
                "normal": AppleColors.GREEN,
                "hover": AppleColors.GREEN_HOVER,
                "pressed": AppleColors.GREEN_PRESSED,
                "disabled": AppleColors.GREEN_DISABLED,
            },
            "danger": {
                "normal": AppleColors.RED,
                "hover": AppleColors.RED_HOVER,
                "pressed": AppleColors.RED_PRESSED,
                "disabled": AppleColors.RED_DISABLED,
            },
            "secondary": {
                "normal": AppleColors.GRAY5,
                "hover": AppleColors.GRAY,
                "pressed": "#D1D1D6",
                "disabled": f"{AppleColors.GRAY5}80",
            },
        }

        set_color = colors.get(self.variant, colors["primary"])
        text_color = "#FFFFFF" if self.variant != "secondary" else AppleColors.LABEL

        filed_style = f"""
            QPushButton {{
                background-color: {set_color['normal']};
                color: {text_color};
                border: none;
                border-radius: 8px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {set_color['hover']};
            }}
            QPushButton:pressed {{
                background-color: {set_color['pressed']};
            }}
            QPushButton:disabled {{
                background-color: {set_color['disabled']};
                color: {text_color};
            }}
        """

        text_style = f"""
            QPushButton {{
                background-color: transparent;
                color: {set_color['normal']};
                border: none;
                font-weight: 500;
            }}
            QPushButton:hover {{
                color: {set_color['hover']};
            }}
            QPushButton:pressed {{
                color: {set_color['pressed']};
            }}
            QPushButton:disabled {{
                color: {set_color['disabled']};
            }}
        """

        style = filed_style if self.type == "filled" else text_style
        self.setStyleSheet(style)

    def _set_size(self):
        sizes = {"small": (80, 32, 12), "medium": (120, 44, 14), "large": (160, 52, 16)}
        min_width, height, font_size = sizes.get(self.size, sizes["medium"])

        current_style = self.styleSheet()
        self.setStyleSheet(
            current_style + f"QPushButton {{ font-size: {font_size}px; }}"
        )

        if self.type == "filled":
            if self.full_width:
                self.setMinimumHeight(height)
                self.setSizePolicy(
                    QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
                )
            else:
                self.setMinimumSize(QtCore.QSize(min_width, height))
                self.setSizePolicy(
                    QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
                )
        else:
            self.setSizePolicy(
                QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
            )
            self.adjustSize()

    def set_icon(
        self, icon: Union[QtGui.QIcon, str], icon_size: Optional[QtCore.QSize] = None
    ):
        self._set_icon(icon, icon_size)
