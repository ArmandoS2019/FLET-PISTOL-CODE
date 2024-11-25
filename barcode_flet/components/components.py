import flet as ft
import time
import requests
from config.config import BASE_URL  # Import BASE_URL from config.py

class MyComponents(ft.Page):
    
    def __init__(self, page):
        self.page = page
        
    def send_save_image_report(self,e):
        self.my_current_user = self.page.client_storage.get("username")
        self.page.launch_url(f'images/download_image/{self.my_current_user}.png')
        self.page.launch_url(f'get_data/')
        # try:
        #     response = requests.get(f'{BASE_URL}/get_data/')
        #     if response.status_code == 200:
        #         data = response.json()
        #         print(data['items'])
        #     else:
        #         print(f"Error: {response.status_code}")
        # except requests.RequestException as e:
        #     print(f"Error de solicitud: {e}") 
             
        return True
    
    def btn_send_report_whatsapp(self,e):
        phone_number="18293871165"
        message="Enviar WhatsApp",
        self.page.launch_url(f"https://wa.me/{phone_number}?text={message}")
        
        # phone_number = "18293871165"
        # self.page.launch_url(f"https://wa.me/18293871165?text=Hello%20from%20FastAPI!")
        return True
       
    def btn_cupertino_status(self):
    
        my_radio_group = ft.CupertinoSegmentedButton(
                padding=10,
                width=9000,
                selected_index=1,
                click_color=self.page.theme.color_scheme.on_tertiary,
                unselected_color=ft.colors.WHITE,
                selected_color=ft.colors.BLUE_900,
                border_color=self.page.theme.color_scheme.on_tertiary,
                on_change=lambda e: print(f"selected_index: {e.data}"),
                controls=[
                    ft.Container(
                        padding=ft.padding.symmetric(0, 30),
                        content=ft.Text("Recibir",  
                                        size=18,
                                        color=self.page.theme.color_scheme.on_tertiary,
                                        font_family="Open Sans",
                                        text_align="center"),
                    ),
                    ft.Container(
                        padding=ft.padding.symmetric(0, 10),
                        content=ft.Text("Despachar", 
                                        size=18,
                                        color=self.page.theme.color_scheme.on_tertiary,
                                        font_family="Open Sans",
                                        text_align="center"),
                    ),
                ],
            )
        
        return ft.Container(content=my_radio_group, 
                            border_radius=12,
                            bgcolor=self.page.theme.color_scheme.on_tertiary_container,
                            alignment=ft.alignment.center)  
    
    def on_submit_modal_status(self, e):
        self.dlg_modal = self.modal_alert_status()
        codigo = self.barcode_input.value
        if codigo == 'a':
            self.dlg_modal = self.modal_alert_status()
            self.page.overlay.append(self.dlg_modal)
            self.dlg_modal.open = True
            self.page.update()
        else:
            self.dlg_modal.open = False
            self.page.update()
            # Limpiar el campo de texto para la siguiente lectura
            self.barcode_input.value = ""
        # Actualizamos la interfaz
        self.page.update()
        return True
    
    
    def show_spinner(self):
        # Create a centered container for the spinner
        spinner_container = ft.Container(
            content=ft.CupertinoActivityIndicator(
            radius=50,
            color=self.page.theme.color_scheme.on_tertiary,
            animating=True ),
            alignment=ft.alignment.center,  # Center the spinner in the container
            width=self.page.width,         # Match the width of the screen
            height=self.page.height,       # Match the height of the screen
        )

        # Add the spinner container to the overlay
        self.page.overlay.append(spinner_container)
        self.page.update()  # Update the page to show the spinner
        return spinner_container

    def hide_spinner(self, spinner):
        if spinner in self.page.overlay:
            self.page.overlay.remove(spinner)
        self.page.update()
    
    def changed_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        # Actualizar el ícono dependiendo del tema actual
        self.btn_popup_change_theme.icon = ft.icons.WB_SUNNY_OUTLINED if self.page.theme_mode == ft.ThemeMode.DARK else ft.icons.NIGHTLIGHT_ROUND
        
        self.page.update()
        return True
    
    def handle_close(self,e):
        self.dlg_modal.open = False
        self.page.close(self.dlg_modal)
        self.page.update()
        self.barcode_input.focus()
        self.barcode_input.value=''
        return True
    
    def handle_close_modal_report(self,e):
        # self.my_modal_show_report.open = False
        self.page.close(self.my_modal_show_report)
        self.page.update()
        self.barcode_input.focus()
        self.barcode_input.value=''
        return True
