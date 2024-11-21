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
        
        def button_clicked(e):
            t.value = f"Your favorite color is:  {cg.value}"
            self.page.update()

        # label_style=ft.TextStyle(
        #                         color=ft.colors.GREEN,
        #                         size=14,
        #                         weight=ft.FontWeight.W_600
        #                     )
        my_radio_group = ft.CupertinoSegmentedButton(
            selected_index=1,
            unselected_color=ft.colors.WHITE,
            selected_color=ft.colors.BLUE_900,
            border_color=ft.colors.BLUE,
            on_change=lambda e: print(f"selected_index: {e.data}"),
            controls=[
                ft.Container(
                    padding=ft.padding.symmetric(0, 30),
                    content=ft.Text("Recibir",  
                                    size=18,
                                    color=ft.colors.BLUE_GREY_100,
                                    font_family="Open Sans",
                                    text_align="center"),
                ),
                ft.Container(
                    padding=ft.padding.symmetric(0, 10),
                    content=ft.Text("Despachar", 
                                    size=18,
                                    color=ft.colors.BLUE_GREY_100,
                                    font_family="Open Sans",
                                    text_align="center"),
                ),
            ],
        )
        # self.btn_cupertino_status = ft.CupertinoNavigationBar(
        # bgcolor=self.page.theme.color_scheme.primary,
        # inactive_color=self.page.theme.color_scheme.on_error,
        # active_color=self.page.theme.color_scheme.secondary,
        # on_change=lambda e: print("Selected tab:", e.control.selected_index),
        #     destinations=[
        #         ft.NavigationBarDestination(icon=ft.icons.MOVE_TO_INBOX,
        #                                     selected_icon=ft.icons.MOVE_TO_INBOX,
        #                                     selected_icon_content=ft.Icon(ft.icons.CHECK, 
        #                                                                   color=self.page.theme.color_scheme.on_tertiary),
        #                                     icon_content=ft.Text("ESTAS DESPACHANDO", size=18, weight="bold"),
        #                                     label="RECIBIR"),
        #         ft.NavigationBarDestination(icon=ft.icons.ARROW_FORWARD, 
        #                                     selected_icon_content=ft.Icon(ft.icons.CHECK, 
        #                                                                   color=self.page.theme.color_scheme.on_tertiary),
        #                                     icon_content=ft.Text("ESTAS RECIBIENDO", size=18, weight="bold"),
        #                                     label="DESPACHAR"),
        #     ] q
        # )
        return ft.Container(content=my_radio_group, alignment=ft.alignment.center)  
    
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
    
    def changed_theme(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        # Actualizar el ícono dependiendo del tema actual
        self.btn_popup_change_theme.icon = ft.icons.WB_SUNNY_OUTLINED if self.page.theme_mode == ft.ThemeMode.DARK else ft.icons.NIGHTLIGHT_ROUND
        
        self.page.update()
        return True
    
    def handle_close(self,e):
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
