import flet as ft

class MyCupertinoActionSheet:

    def __init__(self, page):
        self.page = page
        
    def get_cupertino_action_sheet(self):

        def handle_click(e):
            self.page.close(bottom_sheet)
                
        action_sheet = ft.CupertinoActionSheet(
            title=ft.Row(alignment=ft.MainAxisAlignment.CENTER, 
                         controls=[ft.Text("DOCUMENTOS RECIBIDOS", 
                                  color=self.page.theme.color_scheme.on_tertiary)]),
            message=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                           controls=[ft.Text("Historico de tus documentos recibidos", 
                                  color=self.page.theme.color_scheme.on_tertiary)]),
            cancel=ft.CupertinoActionSheetAction(
                content=ft.Text("Cerrar vista", 
                                  color=self.page.theme.color_scheme.on_tertiary),
                on_click=handle_click,
            ),
            actions=[self.data_table()],

        )

        bottom_sheet = ft.CupertinoBottomSheet(action_sheet)

        return bottom_sheet