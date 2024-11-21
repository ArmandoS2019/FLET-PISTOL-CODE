import flet as ft

class MySnackBar:

    def __init__(self, page):
        self.page = page
        self.my_current_user = self.page.client_storage.get("username")
        
    def close_modal_open_success_snackbar(self,e):
        self.handle_close(e)
        self.insert_data_to_montodb() 
        self.page.snack_bar.open = True
        self.page.snack_bar.bgcolor = self.page.theme.color_scheme.on_tertiary
        self.page.snack_bar.content = self.my_card_snackbar('Recibido exitosamente',
                                                            'Aqui el ID recibido',
                                                            ft.icons.SECURITY_UPDATE_GOOD_ROUNDED)
        self.page.update()     
        return True
    
    def get_snackbar(self):
        self.snackbar = ft.SnackBar(dismiss_direction=ft.DismissDirection.START_TO_END,
                    padding=2,
                    width=400,
                    duration=2000,
                    show_close_icon=True,
                    content=ft.Text('Ultitracking'),
                    bgcolor=self.page.theme.color_scheme.on_tertiary,
                    shape=ft.RoundedRectangleBorder(radius=20), 
                    elevation=5,
                    behavior=ft.SnackBarBehavior.FLOATING)
        return self.snackbar