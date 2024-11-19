import flet as ft

class MyCupertinoActionSheet:

    def __init__(self, page):
        self.page = page
        
    def get_cupertino_action_sheet(self):

        action_sheet = ft.CupertinoActionSheet(
            
            title=ft.Row([ft.Text("DOCUMENTOS RECIBIDOS")], 
                         alignment=ft.MainAxisAlignment.CENTER),
            message=ft.Row([ft.Text("Aqui tienes un historico de tus documentos recibidos")], alignment=ft.MainAxisAlignment.CENTER),
            cancel=ft.CupertinoActionSheetAction(
                content=ft.Text("Cancel"),
                on_click='handle_click',
            ),
            actions=[
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Default Action"),
                    is_default_action=True,
                    on_click='handle_click',
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Normal Action"),
                    on_click='handle_click',
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Destructive Action"),
                    is_destructive_action=True,
                    on_click='handle_click',
                ),
            ],
        )

        bottom_sheet = ft.CupertinoBottomSheet(action_sheet)
    
        return bottom_sheet