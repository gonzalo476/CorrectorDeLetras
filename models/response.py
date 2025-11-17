from dataclasses import dataclass
from typing import Optional


@dataclass
class Response:
    success: bool
    data: Optional[str] = None
    error: Optional[str] = None
