import flet as ft
import cv2
from pyzbar.pyzbar import decode
import os
import re
import requests
from config.config import BASE_URL  # Import BASE_URL from config.py

class MyNavigationRail:

    def __init__(self, page):
        self.page = page
    
    def bucle_barcode(self, image):
        decoded_objects = decode(image)
    
        # Verificar si la lista de objetos decodificados no está vacía
        if decoded_objects:
            # Obtener el último resultado de la lista
            last_result = decoded_objects[-1]  # -1 para obtener el último elemento
            print(f"Último resultado: {last_result}")
            
            # Procesar el contenido si es necesario
            barcode_data = last_result.data.decode('utf-8')
            print(f"Datos del último QR: {barcode_data}")
            return barcode_data
        else:
            print("No se encontraron códigos QR en la imagen.")
            return None  # Devuelve `None` si no hay resultados
        
    def read_barcode(self,e):
        image_path = f"assets/uploads/{e.file_name}"
        
        # Enviar la imagen como archivo en una solicitud POST
        with open(image_path, "rb") as image_file:
            files= {"file": image_file}  # El nombre del campo debe coincidir con el nombre del parámetro en FastAPI
            response = requests.post('http://10.0.0.54:5000/read_qr/read_qr/', files=files)
        # Imprimir la respuesta
        if response.status_code == 200:
            print("Respuesta de la API:", response.json())
        else:
            print("Error:", response.status_code, response.text)
        
        #!88888888888888    
        # # Inicializar el decodificador
        # reader = zxing.BarCodeReader()
        # barcode = reader.decode(image_path)

        # if barcode:
        #     print("Datos decodificados:", barcode.parsed)
        # else:
        #     print("No se encontró ningún código QR.")
        #!88888888888888    
        # Verificar si la imagen existe
        # if not os.path.exists(image_path):
        #     print("Error: La imagen no existe en la ruta especificada.")
        #     return False
        # # Leer la imagen con OpenCV
        # image = cv2.imread(image_path)
        # if image is None:
        #     print("No se encontró ningún código de barras o QR en la imagen.")
        #     return False
        # resultimage = self.bucle_barcode(image)
        # print(type(resultimage))
        # print('****************')
        # print(resultimage)
    
        # # Decodificar códigos de barras y QR en la imagen
        # decoded_objects = decode(image)
        
        # if decoded_objects:
            
        #     for obj in decoded_objects:
        #         barcode_data = obj.data.decode('utf-8')
        #         barcode_type = obj.type
        #         # print(f"Tipo: {barcode_type}, Contenido: {barcode_data}")
                
        #         # Patrón de expresión regular para extraer el valor del parámetro id
        #         pattern = r"id=([A-Z]\d{2}-\d{2}-\d{4})"
        #         # Buscar el patrón en el contenido
        #         resultado = re.search(pattern, barcode_data)
        #         print(resultado)
        #         if resultado.group(1):
        #             self.dlg_modal.open = True
        #             self.page.update()
                   
        # if not decoded_objects:
        #     color = self.page.theme.color_scheme.on_error
        #     self.snackbar_read_qrbarcode(e, 'No se encontró ningún código de barras o QR, vuelva a intentarlo.', color)
        #     self.page.update()
        #     print('Imagen no contiene QR')
        # return True
        
    def upload_files(self,e):
        upload_list = []
        if self.file_picker.result != None and self.file_picker.result.files != None:
            for f in self.file_picker.result.files:
                upload_list.append(
                    ft.FilePickerUploadFile(
                        f.name,
                        upload_url=self.page.get_upload_url(f.name, 600),
                    )
                )
            self.file_picker.upload(upload_list)
            

    def my_navigation_rail(self):
        
        # def openmodal(e):
        #     self.dlg_modal.open = True
        #     self.page.update()
            
        self.dlg_modal = ft.AlertDialog(
                    bgcolor='#040f3d',
                    modal=True,
                    title=ft.Text("Please confirm"),
                    content=ft.Text("Do you really want to delete all those files?"),
                    actions=[self.my_card],
                        actions_alignment=ft.MainAxisAlignment.CENTER)
        self.page.overlay.append(self.dlg_modal)
                   
        self.file_picker = ft.FilePicker(on_result=self.upload_files,
                                         on_upload=self.read_barcode)

        self.upload_message = ft.Text('hola', color=ft.colors.RED)
        self.page.overlay.append(self.file_picker)

        rail = ft.Container(width=50,padding=5,border_radius=4,
                            shadow=ft.BoxShadow(blur_radius=10, spread_radius=5, color=self.page.theme.color_scheme.secondary),
                            bgcolor=self.page.theme.color_scheme.primary,
                            content=ft.Column(alignment=ft.MainAxisAlignment.START,
                                controls=[self.upload_message,
                                    ft.IconButton(icon=ft.icons.ADD_A_PHOTO,
                                    hover_color=ft.colors.LIGHT_BLUE_100,
                                    icon_color=self.page.theme.color_scheme.secondary,
                                    tooltip="Envie foto QR/Cod.Barra",
                                    on_click=lambda _: self.file_picker.pick_files(dialog_title="Enviar QR o CODIGO DE BARRA",
                                                                                    allow_multiple=False, 
                                                                                    file_type=ft.FilePickerFileType.IMAGE)),
                                    ft.IconButton(on_click=self.verify_check_true_datatable,
                                                  hover_color=ft.colors.LIGHT_BLUE_100,
                                                  icon_color=self.page.theme.color_scheme.secondary,
                                                  icon=ft.icons.PICTURE_AS_PDF_ROUNDED,
                                                  tooltip="Seleccione en la tabla RECIBO"),
                                    ft.IconButton(on_click=self.btn_send_report_whatsapp,
                                                  hover_color=ft.colors.LIGHT_BLUE_100,
                                                  icon_color=self.page.theme.color_scheme.secondary,
                                                  icon=ft.icons.SEND,
                                                  tooltip='Enviar recibo por WhatsApp')])) 
        return rail 