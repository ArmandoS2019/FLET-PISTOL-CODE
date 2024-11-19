
import flet as ft
import re
import requests
from config.config import BASE_URL  # Import BASE_URL from config.py


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
            self.dlg_modal.open = True
            self.page.update()
            print("Respuesta de la API:", response.json())
        else:
            if not self.dlg_modal.open:
                color = self.page.theme.color_scheme.on_error
                self.snackbar_read_qrbarcode(e, 'No se encontró ningún código de barras o QR, vuelva a intentarlo.', color)
            print("Error:", response.status_code, response.text)
        return True
        
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
    def get_floating_button(self):
        
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

        self.page.overlay.append(self.file_picker)
        
        self.my_floating_button_send_qr = ft.FloatingActionButton(
        text='Enviar foto QR',
        icon=ft.icons.DOCUMENT_SCANNER_ROUNDED, 
        foreground_color=ft.colors.WHITE,
        opacity=0.9,
        shape=ft.RoundedRectangleBorder(radius=90),
        mini=True,
        on_click=lambda _: self.file_picker.pick_files(
            dialog_title="Enviar QR o CODIGO DE BARRA",
            allow_multiple=False, 
            file_type=ft.FilePickerFileType.IMAGE))
        
        return self.my_floating_button_send_qr