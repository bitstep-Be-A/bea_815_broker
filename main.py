from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schema.main import Img2imgRequestBody, Img2ImgResponse, Status, ImageDataMessageDto
from service.main import create_progress, send_message


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/img2img")
def img2img_api(req: Img2imgRequestBody) -> Img2ImgResponse:
    is_success, response = create_progress(Status.SEND)
    if (not is_success):
        raise HTTPException(status_code=400, detail="progress등록에 실패하였습니다.")

    send_message(ImageDataMessageDto(
        **req.dict(),
        id=response.id
    ))

    return response
