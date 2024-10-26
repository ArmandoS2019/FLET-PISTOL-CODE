from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
class MyReport:
    
    def __init__(self):
        width = 463  # Ancho en píxeles
        height = 1417  # Largo en píxeles (7 pulgadas como ejemplo)
        receive_image = Image.new('RGB', (width, height), (255, 255, 255)).convert("RGBA")
        draw = ImageDraw.Draw(receive_image)
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 26)
            regular_font = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            font = ImageFont.load_default()
            font2 = ImageFont.load_default()

        # Guardar la imagen
        # Cargar el logo (Asegúrate de tener el logo en el mismo directorio)
        logo = Image.open('barcode_flet/assets/logopn.jpg').convert("RGBA")
        logo = logo.resize((130, 100))  # Cambia el tamaño del logo según sea necesario
        # Calcular las coordenadas para centrar el logo en la parte superior
        logo_width, logo_height = logo.size
        center_x = (width - logo_width) // 2
        top_y = 10  # Espacio desde la parte superior

        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        draw.text((50, 110), "P O L I C I A   N A C I O N A L", fill="black", font=title_font)
        draw.text((50, 140), "****     RECIBO EXPEDIENTES     ****", spacing=12, align="right", fill="black", font=regular_font)
        draw.text((50, 170), "* * * * * * * * * * * * * * * * * * * *  * *  * *  * *", fill="black", font=regular_font)
        draw.text((50, 190), f"Fecha: {current_date}", fill="black", font=regular_font)
        draw.text((50, 220), "Usuario: JuanPerez", fill="black", font=regular_font)
        draw.text((50, 240), "-----------------------------------------------------", fill="black", font=regular_font)
        
        # Definir la posición inicial
        x = 50
        y = 260  # Posición vertical inicial
        line_spacing = 30  # Espacio entre líneas

        # Bucle para escribir en la imagen con salto de línea
        my_list_items = range(0, 12)
        for num, dat in enumerate(my_list_items,start=1):
            draw.text((x, y), f"{num}: {dat}", fill="black", font=regular_font)
            y += line_spacing  # Incrementar la posición Y para el siguiente texto
            print(num, dat)
        draw.text((x, y), f"Total: {len(my_list_items)} |||||||||||||||||||||||||||||||||||||||||||||||||||||", fill="black", font=regular_font)
        
        receive_image.paste(logo, (center_x, top_y), logo)  # Cambia las coordenadas según la posición deseada

        receive_image.save('imagen_ejemplo.png')
        # Mostrar la imagen (opcional, si estás en un entorno local)
        receive_image.show()

my_report = MyReport()