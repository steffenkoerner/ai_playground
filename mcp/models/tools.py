
from abc import abstractmethod
from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    description: str

    @abstractmethod
    def schema(self) -> dict:
        ...

    @abstractmethod
    def execute(self, arguments: dict):
        ...