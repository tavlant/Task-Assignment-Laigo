from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.ocr import process_document
from app.utils import format_and_save_response
import aiofiles
import os
import mimetypes

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

SUPPORTED_FILE_TYPES = ["application/pdf", "image/jpeg", "image/png"]

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_type, _ = mimetypes.guess_type(file.filename)
    
    if file_type not in SUPPORTED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    file_location = file.filename
    async with aiofiles.open(file_location, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    try:
        result = await process_document(file_location)
    except Exception as e:
        os.remove(file_location)
        raise HTTPException(status_code=500, detail=f"Error processing document: {e}")
    
    os.remove(file_location)  
    
    base_file_name = os.path.splitext(file.filename)[0]
    formatted_result = format_and_save_response(result, base_file_name)
    return formatted_result

@app.get("/", response_class=HTMLResponse)
async def main():
    with open("static/index.html") as f:
        content = f.read()
    return HTMLResponse(content=content)
