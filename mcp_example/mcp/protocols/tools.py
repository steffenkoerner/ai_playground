
from abc import ABC, abstractmethod
from pydantic import BaseModel


class Tool(BaseModel, ABC):
    name: str
    description: str

    @abstractmethod
    def schema(self) -> dict:
        ...

    @abstractmethod
    def execute(self, arguments: dict):
        ...