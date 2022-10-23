from numpy import extract
from fastapi import FastAPI,APIRouter, File, UploadFile
import shutil
import os
from paddleocr import PaddleOCR

router = APIRouter()

@router.post('/run')
async def inference(img: UploadFile = File(...)):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(img.file, buffer)
    img_path = 'temp.jpg'
    result = ocr.ocr(img_path, cls=True)
    return result

@router.post('/ping')
async def ping():
    return 'Status 200 - Ready'

app = FastAPI()
app.include_router(router)