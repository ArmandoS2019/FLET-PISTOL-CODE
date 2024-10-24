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