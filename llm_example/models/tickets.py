from enum import Enum
from pydantic import BaseModel

class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class Sentiment(str, Enum):
    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"


class Ticket(BaseModel):
    summary: str
    priority: Priority
    sentiment: Sentiment
    suggested_reply: str
