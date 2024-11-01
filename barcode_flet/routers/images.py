from fastapi import APIRouter
from fastapi.responses import FileResponse
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from pyzbar.pyzbar import decode
from PIL import Image
import io

router_image = APIRouter()

# Variable global para almacenar el último frame capturado
latest_frame = None

@router_image.get("/download_image/{nombre_imagen}")
async def dowload_image(nombre_imagen: str):
    # Ruta de la imagen en el sistema de archivos local
    IMAGE_PATH = os.path.join("assets/image_report", f"{nombre_imagen}") 
    if not os.path.exists(IMAGE_PATH):
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    return FileResponse(IMAGE_PATH, media_type="image/png", filename=nombre_imagen)

@router_image.post("/read_qr/")
async def read_qr(file: UploadFile = File(...)):
    # Check if the uploaded file is an image
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    # Read the file and convert it to a PIL image
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    
    # Decode the QR code
    decoded_objects = decode(image)
    
    # Check if any QR codes were found
    if not decoded_objects:
        raise HTTPException(status_code=404, detail="No QR code found in the image.")
    
    # Extract and return the QR code data
    qr_data = [{"data": obj.data.decode("utf-8"), "type": obj.type} for obj in decoded_objects]
    return {"qr_codes": qr_data}

