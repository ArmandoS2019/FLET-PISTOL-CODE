import flet as ft


class BottomAppBar:
    
    def __init__(self, page):
        self.page = page

    def get_bottom_appbar(self):
    
        bottom_app_bar = ft.BottomAppBar(
                        height=60,
                        bgcolor=self.page.theme.color_scheme.secondary,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(on_click=self.verify_check_true_datatable,
                                                  hover_color=ft.colors.ORANGE_300,
                                                  icon_color=ft.colors.WHITE,
                                                  icon=ft.icons.PICTURE_AS_PDF_ROUNDED,
                                                  tooltip="Seleccione en la tabla RECIBO"),
                                    ft.IconButton(on_click=self.btn_send_report_whatsapp,
                                                  hover_color=ft.colors.ORANGE_300,
                                                  icon_color=ft.colors.WHITE,
                                                  icon=ft.icons.SEND,
                                                  tooltip='Enviar recibo por WhatsApp'),
                                ft.Container(expand=True),
                                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE,
                                              tooltip='Buscar registro',
                                              hover_color=ft.colors.ORANGE_300),
                                ft.IconButton(icon=ft.icons.COMMENT_OUTLINED, 
                                              icon_color=ft.colors.WHITE,
                                              tooltip='Registros anteriores',
                                              hover_color=ft.colors.ORANGE_300,
                                              on_click=lambda e: self.page.open(self.get_cupertino_action_sheet())),
                            ]
                        ),
                    )
        return bottom_app_bar