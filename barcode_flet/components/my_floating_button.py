
import flet as ft
import re
import requests
from config.config import BASE_URL  # Import BASE_URL from config.py
from time import sleep


class MyFloatinButton:
    
    def __init__(self, page):
        self.page = page
    
    def read_barcode(self,e):
        
        image_path = f"assets/uploads/{e.file_name}"
        # Enviar la imagen como archivo en una solicitud POST
        with open(image_path, "rb") as image_file:
            files= {"file": image_file}  # El nombre del campo debe coincidir con el nombre del parámetro en FastAPI
            response = requests.post(f'{BASE_URL}/read_qr/read_qr/', files=files)
        # Imprimir la respuesta
        if response.status_code == 200:
            if not self.dlg_modal.open:
                # self.spinner = self.show_spinner()
                self.dlg_modal.open = True
                # sleep(0.9)
                # self.hide_spinner( self.spinner)
                self.hide_spinner(self.spinner)
                print("Respuesta de la API:", response.json())
        else:               
            # self.hide_spinner(self.spinner)              
            if not self.dlg_modal.open:
                self.page.snack_bar.open = True
                self.page.snack_bar.bgcolor = self.page.theme.color_scheme.on_error
                self.page.snack_bar.content = self.my_card_snackbar('QR NO ENCONTRADO',
                                                                    'Vuelva a Intentarlo',
                                                                    ft.icons.GPP_BAD_OUTLINED)
        self.hide_spinner(self.spinner)              
                
    def upload_files(self,e):
        self.spinner = self.show_spinner()
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
            
    def get_floating_button(self):
        
        self.dlg_modal = self.modal_alert_status()
        self.page.overlay.append(self.dlg_modal)
        self.page.update()
        
        self.file_picker = ft.FilePicker(on_result=self.upload_files,
                                         on_upload=self.read_barcode)
       

        self.page.overlay.append(self.file_picker)
        
        self.my_floating_button_send_qr = ft.FloatingActionButton(
        content=ft.Icon(name=ft.icons.CAMERA_ALT, 
                        color=ft.colors.LIGHT_GREEN_ACCENT_400, size=40),
        foreground_color=ft.colors.RED,
        bgcolor=self.page.theme.color_scheme.on_tertiary_container,
        height=56,
        width=56,
        opacity=0.9,
        shape=ft.RoundedRectangleBorder(radius=50),
        mini=True,
        on_click=lambda _: self.file_picker.pick_files(
            dialog_title="Enviar QR o CODIGO DE BARRA",
            allow_multiple=False, 
            file_type=ft.FilePickerFileType.IMAGE))
        
        return ft.Container(
                            self.my_floating_button_send_qr,
                            border=ft.border.all(2, self.page.theme.color_scheme.on_tertiary),
                            border_radius=ft.border_radius.all(50),
                            padding=5,  # Agrega espacio alrededor del botón
                            ink=True  # Activa el efecto de onda al hacer clic
                        )  # Espacio entre el borde y el contenido)