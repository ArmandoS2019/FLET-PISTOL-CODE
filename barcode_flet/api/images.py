from fastapi import APIRouter
from fastapi.responses import FileResponse
import os
from fastapi import FastAPI, File, UploadFile, HTTPException,Request
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError  # Asegúrate de importar UnidentifiedImageError
import io
import cv2
import numpy as np

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
    
    allowed_extensions = ["jpg", "jpeg", "png", "bmp"]
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        raise HTTPException(
            status_code=400, 
            detail="El archivo debe ser una imagen con extensión: .jpg, .jpeg, .png o .bmp."
        )

    print("Archivo recibido:", file.filename)
    try:
        # Leer los datos del archivo una sola vez
        image_data = await file.read()
        # Abrir y validar la imagen en un solo paso
        image = Image.open(io.BytesIO(image_data))
        image.load()  # Carga los datos de la imagen para validar su integridad
    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="El archivo no es una imagen válida o está dañado. Asegúrate de subir un archivo de imagen soportado como JPG o PNG."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado al procesar la imagen: {str(e)}"
        )
    # Decodificar el código QR
    decoded_objects = decode(image)
    # Verificar si se encontraron códigos QR
    if not decoded_objects:
        raise HTTPException(status_code=404, detail="No QR code found in the image.")
    
    # Extraer y devolver los datos del código QR
    qr_data = [{"data": obj.data.decode("utf-8"), "type": obj.type} for obj in decoded_objects]
    return JSONResponse(content={"qr_codes": qr_data})



@router_image.get("/camera", response_class=HTMLResponse)
async def get_camera():
    html_content = """<!DOCTYPE html>        
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Lectura de Códigos QR</title>
                        </head>
                        <body>
                            <h1>Lectura de Códigos QR</h1>
                            <p>Coloca un código QR frente a la cámara para escanearlo.</p>
                            <video id="video" width="640" height="480" autoplay></video>
                            <p id="result">Resultado del QR: Ninguno</p>

                            <script>
                                const video = document.getElementById("video");
                                const result = document.getElementById("result");

                                // Acceder a la cámara
                                navigator.mediaDevices.getUserMedia({ video: true })
                                    .then((stream) => {
                                        video.srcObject = stream;

                                        // Crear un canvas para capturar fotogramas
                                        const canvas = document.createElement("canvas");
                                        const context = canvas.getContext("2d");

                                        // Capturar y enviar fotogramas al servidor cada 500 ms
                                        setInterval(() => {
                                            canvas.width = video.videoWidth;
                                            canvas.height = video.videoHeight;
                                            context.drawImage(video, 0, 0, canvas.width, canvas.height);

                                            // Convertir el fotograma a formato Base64
                                            const imageData = canvas.toDataURL("image/jpeg");

                                            // Enviar el fotograma al backend para detección de QR
                                            fetch("/process-image", {
                                                method: "POST",
                                                headers: {
                                                    "Content-Type": "application/json"
                                                },
                                                body: JSON.stringify({ image: imageData })
                                            })
                                            .then((response) => response.json())
                                            .then((data) => {
                                                if (data.qr_result) {
                                                    result.textContent = "Resultado del QR: " + data.qr_result;
                                                } else {
                                                    result.textContent = "Resultado del QR: Ninguno";
                                                }
                                            })
                                            .catch((error) => console.error("Error al procesar la imagen:", error));
                                        }, 500);
                                    })
                                    .catch((err) => {
                                        console.error("Error al acceder a la cámara:", err);
                                    });
                            </script>
                        </body>
                        </html>
                    """

    return HTMLResponse(content=html_content)


import base64
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pyzbar.pyzbar import decode
import cv2
import numpy as np

@router_image.post("/process-image")
async def process_image(request: Request):
    try:
        print(data)
        # Leer los datos de la solicitud
        data = await request.json()
        if "image" not in data:
            return JSONResponse({"error": "La clave 'image' no está en el cuerpo de la solicitud"}, status_code=400)
        
        # Decodificar la imagen Base64
        image_data = data["image"].split(",")[1]
        image_bytes = base64.b64decode(image_data)
        np_img = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        
        # Decodificar el QR usando Pyzbar
        decoded_objects = decode(img)

        # Procesar los resultados
        qr_result = None
        for obj in decoded_objects:
            qr_result = obj.data.decode("utf-8")
            break

        # Devolver el resultado del QR
        if qr_result:
            print(f"Código QR detectado: {qr_result}")
            return JSONResponse({"qr_result": qr_result})
        else:
            print("No se detectaron códigos QR")
            return JSONResponse({"qr_result": None})

    except Exception as e:
        print(f"Error procesando la imagen: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)
    
    
