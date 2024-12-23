import flet as ft

class MyModal:

    def __init__(self, page):
        self.page = page
        
    def modal_alert_status(self):
        self.dlg_modal = ft.AlertDialog(
        bgcolor='#040f3d',
        modal=True,
        title=ft.Text("Por favor confirme si deseea\nrecibir este expediente", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Realmente desea recibir este expediente?"),
        actions=[self.my_card],
        actions_alignment=ft.MainAxisAlignment.CENTER)
        return self.dlg_modal
    
    def modal_show_report(self, image):      
        
        self.my_modal_show_report = ft.AlertDialog(
        bgcolor=self.page.theme.color_scheme.secondary,
        modal=True,
        title=ft.Text("Usuario: Armando S.\nImprima su reporte", size=15, color="#FFCC00", italic=True),
        content=image,
        actions=[
                ft.ElevatedButton(text='Descargar',
                                  icon=ft.icons.DOWNLOAD, on_click=self.send_save_image_report),
                
                ft.TextButton("Cerrar", on_click=self.handle_close_modal_report, 
                                icon=ft.icons.CANCEL,  
                                icon_color=self.page.theme.color_scheme.on_error,
                                style=ft.ButtonStyle(color=self.page.theme.color_scheme.on_error))],
        actions_alignment=ft.MainAxisAlignment.CENTER)
        return self.my_modal_show_report