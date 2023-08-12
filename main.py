from fastapi import HTTPException

from app import instance

from schema.main import Img2imgRequestBody, Img2ImgResponse, Status, ImageDataMessageDto
from service.main import create_progress, send_message


@instance.post("/api/v1/img2img")
def img2img_api(req: Img2imgRequestBody) -> Img2ImgResponse:
    is_success, response = create_progress(Status.SEND)
    if (not is_success):
        raise HTTPException(status_code=400, detail="progress등록에 실패하였습니다.")

    send_message(ImageDataMessageDto(
        **req.dict(),
        id=response.id
    ))

    return response
