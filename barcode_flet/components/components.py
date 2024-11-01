import flet as ft
import time

class MyComponents(ft.Page):
    
    def __init__(self, page):
        self.page = page
        
    def send_save_image_report(self,e):
        self.my_current_user = self.page.client_storage.get("username").lower()
        self.page.launch_url(f'images/download_image/{self.my_current_user}.png')
        return True
    
    def btn_send_report_whatsapp(self,e):
        # Image URL (hosted online) to send
        # image_url = "https://example.com/path/to/your/image.jpg"
        phone_number = "18293871165"
        
        # WhatsApp link with message text including the image URL
        # whatsapp_link = f"https://wa.me/{phone_number}?text=Check out this image: {image_url}"
    
        self.page.launch_url(f"https://wa.me/18293871165?text=Hello%20from%20FastAPI!")
        return True
       
    def btn_cupertino_status(self):
        self.btn_cupertino_status = ft.CupertinoNavigationBar(
        bgcolor=self.page.theme.color_scheme.primary_container,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.YELLOW_ACCENT_700,
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.MOVE_TO_INBOX,
                                            selected_icon=ft.icons.MOVE_TO_INBOX, 
                                            label="RECIBIR"),
                ft.NavigationBarDestination(icon=ft.icons.ARROW_FORWARD, 
                                            label="DESPACHAR"),
            ]
        )
        return self.btn_cupertino_status    
    
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
