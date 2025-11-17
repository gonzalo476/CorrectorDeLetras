from qtpy import QtWidgets, QtCore
from typing import Literal, Optional
from config.colors import AppleColors


class Button(QtWidgets.QPushButton):
    def __init__(
        self,
        text: str = "Button",
        variant: Literal["primary", "success", "danger", "secondary"] = "primary",
        type: Literal["filled", "text"] = "filled",
        size: Literal["small", "medium", "large"] = "small",
        full_width: bool = False,
        parent: Optional[QtWidgets.QWidget] = None,
    ):
        super().__init__(text, parent)

        self.variant = variant
        self.size = size
        self.full_width = full_width
        self.type = type

        self._set_style()
        self._set_size()

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
