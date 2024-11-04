import flet as ft


class MyNavigationRail:

    def __init__(self, page):
        self.page = page
        
    def my_navigation_rail(self):
        
        def pick_files_result(e: ft.FilePickerResultEvent): 
            selected_files.value = ( ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" ) 
            selected_files.update()
        
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "No selecciono!"
            )
            self.snackbar_read_qrbarcode(e,'Si lei el codigo Open Modal')
            selected_files.update()

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()
        self.page.add(selected_files)
        self.page.overlay.append(pick_files_dialog)

        self.mypicker=ft.Row(alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.ElevatedButton(
                        "Suba una \nfoto QR",
                        icon=ft.icons.ADD_A_PHOTO,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),
                    selected_files,
                ],
            )
        
        rail = ft.Container(width=50,padding=5,border_radius=4,
                            shadow=ft.BoxShadow(blur_radius=10, spread_radius=5, color=self.page.theme.color_scheme.secondary),
                            bgcolor=self.page.theme.color_scheme.primary,
                            content=ft.Column(alignment=ft.MainAxisAlignment.START,
                                controls=[
                                    ft.IconButton(icon=ft.icons.ADD_A_PHOTO,
                                                  icon_color=self.page.theme.color_scheme.secondary,
                                                  tooltip="Envie foto QR/Cod.Barra",
                                                  on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True)),
                                    ft.IconButton(on_click=self.verify_check_true_datatable,
                                                  icon_color=self.page.theme.color_scheme.secondary,
                                                  icon=ft.icons.PICTURE_AS_PDF_ROUNDED,
                                                  tooltip="Seleccione en la tabla RECIBO"),
                                    ft.IconButton(on_click=self.btn_send_report_whatsapp,
                                                  icon_color=self.page.theme.color_scheme.secondary,
                                                  icon=ft.icons.SEND,
                                                  tooltip='Enviar recibo por WhatsApp')])) 
        return rail 