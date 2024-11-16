import flet as ft


class MyCard:

    def __init__(self, page):
        self.page = page
        
    def my_card(self):
        self.mycard = ft.Card(
            content=ft.Container(bgcolor="#04396b",
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DESCRIPTION),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Recibir", on_click=self.snackbar_success, 
                                icon=ft.icons.CHECK_CIRCLE,
                                icon_color=ft.colors.YELLOW_ACCENT_200, 
                                style=ft.ButtonStyle(color=ft.colors.YELLOW_ACCENT_200)), 
                             ft.TextButton("Cerrar", on_click=self.handle_close, 
                                icon=ft.icons.CANCEL,  
                                icon_color=self.page.theme.color_scheme.on_error,
                                style=ft.ButtonStyle(color=self.page.theme.color_scheme.on_error))],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        return self.mycard
        