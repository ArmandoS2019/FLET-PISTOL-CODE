import flet as ft

class MySnackBar:

    def __init__(self, page):
        self.page = page
        self.my_current_user = self.page.client_storage.get("username")
        
    def snackbar_read_qrbarcode(self, e, message, color):
        
        self.my_qr_data_card =ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DESCRIPTION),
                            title=ft.Text("No se detecto lectura de algun QR"),
                            subtitle=ft.Text(
                                "Trate de enfocar la camara al QR y enviela nueva vez."
                            ),
                        ),
                        ]
                )
            )
        )
        #!AGREGAR EL SNACKBAR Y LUEGO SOLO ACTIVARLO TRUE
        self.snackbar_success_barcode = ft.SnackBar(
            duration=2000,
            show_close_icon=True,
            content=self.my_qr_data_card,
            bgcolor=color,
            action_color=ft.colors.RED,
            close_icon_color=ft.colors.BLUE_900,
            shape=ft.RoundedRectangleBorder(radius=10), 
            elevation=6,
            behavior=ft.SnackBarBehavior.FLOATING)
        
        self.page.snack_bar = self.snackbar_success_barcode
        self.page.snack_bar.open = True
        self.page.update()
        return self.snackbar_success_barcode    
        
    def snackbar_success(self,e):
        self.handle_close(e)
        self.insert_data_to_montodb() 
        
        self.page.snack_bar.open = True
        self.page.snack_bar.bgcolor = self.page.theme.color_scheme.on_error
        self.page.snack_bar.content = self.my_card_snackbar('QR NO ENCONTRADO','Vuelva a Intentarlo')
        self.page.update()     
                
        # self.my_current_user = self.page.client_storage.get("username")
      
        # # btn_snackbars=ft.Row(
        # #     controls=[
        # #         ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINED, color=self.page.theme.color_scheme.secondary, size=24),  # Ícono de éxito
        # #         ft.Text('Recibido exitosamente', size=16)],
        # #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        # self.snackbar = ft.SnackBar(
        #                         duration=2000,
        #                         show_close_icon=True,
        #                         content=ft.Row([
        #                                         ft.Icon(name=ft.icons.CHECK_CIRCLE, color=ft.colors.WHITE),  # Ícono de información
        #                                         ft.Text(f"Recibido exitosamente por:"),
        #                                         ft.Text(f"{self.my_current_user}.", 
        #                                                 size=20, color="#333333", italic=True),
        #                                     ]),
        #                         bgcolor=self.page.theme.color_scheme.on_tertiary,
        #                         shape=ft.RoundedRectangleBorder(radius=10), 
        #                         elevation=5,
        #                         behavior=ft.SnackBarBehavior.FLOATING)
        
        # # self.page.snack_bar.open = True
        # self.page.snack_bar = self.snackbar
        # self.page.snack_bar.open = True
        # self.page.update()
        
        # self.page.overlay.append(self.snackbar)
        # self.snackbar.open = True
        # self.page.update()
        return True
    
    def get_snackbar(self):
        self.snackbar = ft.SnackBar(
                    width=400,
                    padding=2,
                    duration=2000,
                    show_close_icon=True,
                    content=ft.Text('Ultitracking'),
                    bgcolor=self.page.theme.color_scheme.on_tertiary,
                    shape=ft.RoundedRectangleBorder(radius=10), 
                    elevation=5,
                    behavior=ft.SnackBarBehavior.FLOATING)
        return self.snackbar