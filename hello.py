import cv2
from pyzbar.pyzbar import decode

def read_barcode(image_path):
        # Leer la imagen usando OpenCV
        image = cv2.imread(image_path)

        # Decodificar códigos de barras y QR en la imagen
        decoded_objects = decode(image)

        # Verificar si se encontraron códigos de barras o QR
        if decoded_objects:
            for obj in decoded_objects:
                barcode_data = obj.data.decode('utf-8')
                barcode_type = obj.type
                print(f"Tipo: {barcode_type}, Contenido: {barcode_data}")
        else:
            print("No se encontró ningún código de barras o QR en la imagen.")
        return True
    
    
read_barcode('barcode_flet/uploads/Screenshot 2024-10-30 223258.png')