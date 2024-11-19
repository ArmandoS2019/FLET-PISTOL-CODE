import flet as ft


class BottomAppBar:
    
    def __init__(self, page):
        self.page = page

    def get_bottom_appbar(self):
    
        bottom_app_bar = ft.BottomAppBar(
                        bgcolor=ft.colors.BLUE,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(on_click=self.verify_check_true_datatable,
                                                  hover_color=ft.colors.LIGHT_BLUE_100,
                                                  icon_color=ft.colors.WHITE,
                                                  icon=ft.icons.PICTURE_AS_PDF_ROUNDED,
                                                  tooltip="Seleccione en la tabla RECIBO"),
                                    ft.IconButton(on_click=self.btn_send_report_whatsapp,
                                                  hover_color=ft.colors.LIGHT_BLUE_100,
                                                  icon_color=ft.colors.WHITE,
                                                  icon=ft.icons.SEND,
                                                  tooltip='Enviar recibo por WhatsApp'),
                                ft.Container(expand=True),
                                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                            ]
                        ),
                    )
            
        return bottom_app_bar