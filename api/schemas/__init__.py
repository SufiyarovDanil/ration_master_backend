from pydantic import BaseModel, Field, computed_field
from typing import Any


class OutputSchema(BaseModel):
    data: dict[str, Any] | None = Field(default=None)

    def __init__(self,
                 data: dict[str, Any] | None = None,
                 error: dict[str, str] | None = None):
        super().__init__(data=data, error=error)
        self.data = data
        self.error = error
    
    @computed_field
    @property
    def error(self) -> dict[str, str] | None:
        return self._error
    
    @error.setter
    def error(self, value: str | None) -> None:
        self._error = value if value is None else {'message': value}
