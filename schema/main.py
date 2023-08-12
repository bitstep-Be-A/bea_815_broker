from typing import Optional
from enum import Enum
from pydantic import BaseModel, validator, ValidationError


class Img2imgRequestBody(BaseModel):
    base_image: str
    roop_image: str
    face_index: int

    @validator('base_image', 'roop_image')
    def validate_blank(cls, v):
        if not bool(v):
            raise ValidationError("image should not blank")
        return v


class Img2ImgResponse(BaseModel):
    id: str


class Status(Enum):
    LOADING = "loading"
    ERROR = "error"
    SUCCESS = "success"
    DONE = "done"
    SEND = "send"


class ImageProgress(BaseModel):
    _id: str
    status: str
    imageUrl: str
    worker: Optional[str] = None

    @validator('status')
    def validate_status(cls, v):
        for _, member in Status.__members__.items():
            if member.value == v:
                return v
        raise ValidationError("status value is invalid")


class ImageDataMessageDto(Img2imgRequestBody):
    id: str
