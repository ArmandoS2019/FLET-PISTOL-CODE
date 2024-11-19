import flet as ft

class MyNavigationDrawer:

    def __init__(self, page):
        self.page = page
        
    def get_navigaion_drawer(self):
        # Crear un BottomSheet con contenido
        bottom_sheet = ft.BottomSheet(
                elevation=500,
                content=ft.Container(
                    padding=50,
                    content=ft.Column(
                        tight=True,
                        controls=[
                            ft.Text("This is bottom sheet's content!"),
                            ft.ElevatedButton("Close bottom sheet", on_click=lambda _: page.close(bs)),
                        ],
                    ),
                ),
            )
        return bottom_sheet