import flet as ft

class MyModal:

    def __init__(self, page):
        self.page = page
        
    def modal_alert_status(self):
        self.dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[self.my_card],
        actions_alignment=ft.MainAxisAlignment.CENTER)
        return self.dlg_modal
    
    def modal_show_report(self, image):
        self.my_modal_show_report = ft.AlertDialog(
        modal=True,
        title=ft.Text("Usuario: Armando S.\nImprima su reporte", size=15, color="#FFCC00", italic=True),
        content=image,
        actions=[
                ft.ElevatedButton(text='Imprimir',
                                  icon=ft.icons.PRINT),
                ft.TextButton("Rechazar", on_click=self.handle_close_modal_report, 
                                icon=ft.icons.CANCEL,  
                                icon_color=self.page.theme.color_scheme.on_error,
                                style=ft.ButtonStyle(color=self.page.theme.color_scheme.on_error))],
        actions_alignment=ft.MainAxisAlignment.CENTER)
        return self.my_modal_show_report