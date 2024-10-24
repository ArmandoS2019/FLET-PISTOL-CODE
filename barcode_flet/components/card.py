import flet as ft


class MyCard:

    def __init__(self, page):
        self.page = page
        
    def my_card(self):
        self.mycard = ft.Card(
            content=ft.Container(
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
                                icon_color=self.page.theme.color_scheme.secondary, 
                                style=ft.ButtonStyle(color=self.page.theme.color_scheme.secondary)), 
                             ft.TextButton("Rechazar", on_click=self.handle_close, 
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
        