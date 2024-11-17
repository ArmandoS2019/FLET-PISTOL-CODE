import flet as ft

class MySnackBar:

    def __init__(self, page):
        self.page = page
        self.my_current_user = self.page.client_storage.get("username").lower()
        
    def snackbar_read_qrbarcode(self, e, message, color):
        self.my_current_user = self.page.client_storage.get("username")       
        self.page.snack_bar = ft.SnackBar(
            duration=4500,
            show_close_icon=True,
            content=ft.Row([
                            ft.Icon(name=ft.icons.CHECK_CIRCLE, color=ft.colors.WHITE),  # Ícono de información
                            ft.Text(message),
                            ft.Text(f"{self.my_current_user}.", 
                                    size=20, color="#333333", italic=True),
                        ]),
            bgcolor=color,
            shape=ft.RoundedRectangleBorder(radius=10), 
            elevation=6,
            behavior=ft.SnackBarBehavior.FLOATING)
        self.page.snack_bar.open = True
        self.page.update()
        return True    
        
    def snackbar_success(self,e):
        self.handle_close(e)
        self.insert_data_to_montodb() 
        self.my_current_user = self.page.client_storage.get("username")
      
        # btn_snackbars=ft.Row(
        #     controls=[
        #         ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINED, color=self.page.theme.color_scheme.secondary, size=24),  # Ícono de éxito
        #         ft.Text('Recibido exitosamente', size=16)],
        #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        
        self.snackbar = ft.SnackBar(
                                duration=2000,
                                show_close_icon=True,
                                content=ft.Row([
                                                ft.Icon(name=ft.icons.CHECK_CIRCLE, color=ft.colors.WHITE),  # Ícono de información
                                                ft.Text(f"Recibido exitosamente por:"),
                                                ft.Text(f"{self.my_current_user}.", 
                                                        size=20, color="#333333", italic=True),
                                            ]),
                                bgcolor=self.page.theme.color_scheme.on_tertiary,
                                shape=ft.RoundedRectangleBorder(radius=10), 
                                elevation=5,
                                behavior=ft.SnackBarBehavior.FLOATING)
        
        # self.page.snack_bar.open = True
        self.page.overlay.append(self.snackbar)
        self.snackbar.open = True
        self.page.update()
        return True