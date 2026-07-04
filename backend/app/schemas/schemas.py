from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    id: int
    url: str
    created_at: datetime

    class Config:
        from_attributes = True


class URLStatusResponse(BaseModel):
    id: int
    url: str

    status: str

    status_code: Optional[int]

    response_time: Optional[float]

    last_checked: Optional[datetime]

    error_message: Optional[str]

    class Config:
        from_attributes = True