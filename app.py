from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


instance = FastAPI()

origins = [
    "*"
]

instance.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)