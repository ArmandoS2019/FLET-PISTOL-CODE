from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import flet as ft
import io
import base64


class MyReport:
    
    def __init__(self):
        pass
    
    def get_image_report(self, my_list_items):
        width = 463  # Ancho en píxeles
        height = 980  # Largo en píxeles (7 pulgadas como ejemplo)
        self.receive_image = Image.new('RGB', (width, height), (255, 255, 255)).convert("RGBA")
        self.draw = ImageDraw.Draw(self.receive_image)
        self.current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.number_report = datetime.now().strftime("PN-%Y%m%d%H%M%S")
        try:
            title_font = ImageFont.truetype("arialbd.ttf", 26)
            title_font2 = ImageFont.truetype("arialbd.ttf", 20)
            regular_font = ImageFont.truetype("arial.ttf", 20)
            regular_font2 = ImageFont.truetype("arial.ttf", 15)
        except IOError:
            title_font = ImageFont.load_default()
            title_font2 = ImageFont.load_default()
            regular_font = ImageFont.load_default()
            regular_font2 = ImageFont.load_default()

        # Cargar el logo (Asegúrate de tener el logo en el mismo directorio)
        self.logo = Image.open('assets/logopn.jpg').convert("RGBA")
        self.logo = self.logo.resize((130, 100))  # Cambia el tamaño del logo según sea necesario
        # Calcular las coordenadas para centrar el logo en la parte superior
        logo_width, logo_height = self.logo.size
        self.center_x = (width - logo_width) // 2
        self.top_y = 10  # Espacio desde la parte superior

        self.draw.text((50, 110), "P O L I C I A   N A C I O N A L", fill="black", font=title_font)
        self.draw.text((50, 140), "****   RECEPCION DE EXPEDIENTES   ****", spacing=12, align="right", fill="black", font=regular_font)
        self.draw.text((50, 170), "* * * * * * * * * * * * * * * * * * * *  * *  * *  * *", fill="black", font=regular_font)
        self.draw.text((50, 190), f"Nº: {self.number_report}", fill="black", font=regular_font)
        self.draw.text((50, 215), f"Fecha: {self.current_date}", fill="black", font=regular_font)
        self.draw.text((50, 240), "Usuario: JuanPerez", fill="black", font=regular_font)
        self.draw.text((50, 260), "------------------DETALLE--------------------", fill="black", font=title_font2)
        # Definir la posición inicial
        x = 50
        y = 285  # Posición vertical inicial
        line_spacing = 30  # Espacio entre líneas

        # Bucle para escribir en la imagen con salto de línea
        # my_list_items = range(0, 12)
        for num, dat in enumerate(my_list_items,start=1):
            self.draw.text((x, y), f"{num} - {dat}", fill="black", font=regular_font)
            y += line_spacing  # Incrementar la posición Y para el siguiente texto
           
        
        self.receive_image.paste(self.logo, (self.center_x, self.top_y), self.logo)  # Cambia las coordenadas según la posición deseada
        # self.receive_image.save('imagen_ejemplo.png')
        # Mostrar la imagen (opcional, si estás en un entorno local)
        self.draw.text((x, y), f"Total: {len(my_list_items)}", fill="black", font=title_font2)
        self.draw.text((x, y+15), f"----------------------", fill="black", font=regular_font)
        self.draw.text((x, y+60), f"Firma:__________________________", fill="black", font=title_font2)
        self.draw.text((x, y+100), f"* * * * * * * * * * * * * * * * * * * *  * *  * *  * *", fill="black", font=regular_font)
        self.draw.text((x, y+114), f'''Av. Leopoldo Navarro 402,Santo Domingo 
        10203 Teléfono: (809) 682-2151''', fill="black", font=regular_font2, align='left')
        # Crear un buffer en memoria
        buffered = io.BytesIO()
        # Guardar la imagen en el buffer como PNG
        self.receive_image.save(buffered, format="PNG")
        # Obtener los datos binarios del buffer
        img_data = buffered.getvalue()
        # Codificar en base64 y decodificar para obtener una cadena de texto
        img_str = base64.b64encode(img_data).decode("utf-8")
        return img_str

