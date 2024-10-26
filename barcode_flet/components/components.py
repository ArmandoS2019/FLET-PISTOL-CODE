import flet as ft
import time

class MyComponents(ft.Page):
    
    def __init__(self, page):
        self.page = page
    
    def btn_cupertino_status(self):
        self.btn_cupertino_status = ft.CupertinoSlidingSegmentedButton(
            thumb_color=self.page.theme.color_scheme.tertiary,
            selected_index=1,  # Color del thumb (círculo)
            on_change=lambda e: print(f"selected_index: {e.data}"),
            padding=ft.padding.symmetric(0, 10),
            controls=[
                ft.Text("RECIBIR"),
                ft.Text("DESPACHAR"),
            ])
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
