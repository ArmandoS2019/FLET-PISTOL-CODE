import flet as ft
import cv2
from pyzbar.pyzbar import decode
import os
class MyNavigationRail:

    def __init__(self, page):
        self.page = page
    
    def read_barcode(self,e):
        image_path = f"assets/uploads/{e.file_name}"
        # Verificar si la imagen existe
        if not os.path.exists(image_path):
            print("Error: La imagen no existe en la ruta especificada.")
            return
        # Leer la imagen con OpenCV
        image = cv2.imread(image_path)
        if image is None:
            print("Error: No se pudo cargar la imagen. Verifica la ruta y el formato.")
            return
        # Decodificar códigos de barras y QR en la imagen
        decoded_objects = decode(image)
        if decoded_objects:
            for obj in decoded_objects:
                barcode_data = obj.data.decode('utf-8')
                barcode_type = obj.type
                print(f"Tipo: {barcode_type}, Contenido: {barcode_data}")
        else:
            print("No se encontró ningún código de barras o QR en la imagen.")
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
                                                  on_click=lambda _: self.file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)),
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