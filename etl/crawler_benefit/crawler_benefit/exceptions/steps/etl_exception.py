from typing import Any


class EtlException(Exception):
    def __init__(self, stage: str, data: Any, message: str):
        super().__init__(message)
        self.stage = stage
        self.data = data
        self.message = message
