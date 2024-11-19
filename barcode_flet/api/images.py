from fastapi import APIRouter
from fastapi.responses import FileResponse
import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError  # Asegúrate de importar UnidentifiedImageError
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
    print("Archivo recibido:", file.filename)
    # Leer el archivo y convertirlo a una imagen de PIL
    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        image.verify()  # Verifica si es una imagen válida
        image = Image.open(io.BytesIO(image_data))  # Reabrir la imagen para usarla
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="El archivo no es una imagen válida o está dañado.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar la imagen: {str(e)}")

    # Decodificar el código QR
    decoded_objects = decode(image)

    # Verificar si se encontraron códigos QR
    if not decoded_objects:
        raise HTTPException(status_code=404, detail="No QR code found in the image.")
    
    # Extraer y devolver los datos del código QR
    qr_data = [{"data": obj.data.decode("utf-8"), "type": obj.type} for obj in decoded_objects]
    return JSONResponse(content={"qr_codes": qr_data})

