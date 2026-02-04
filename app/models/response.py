from typing import Any, Optional

class ApiResponse:
    def __init__(
        self,
        success: bool,
        data: Optional[Any] = None,
        message: Optional[str] = None
    ):
        self.success = success
        self.data = data
        self.message = message
        self.count = len(data) if isinstance(data, list) else 0

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "count": self.count,
            "data": self.data,
            "message": self.message
        }