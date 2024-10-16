import flet as ft


class AppBar:

    def __init__(self, page):
        self.page = page
        # my_appbar = self.create_appbar()
        # self.page.appbar = my_appbar 

    def create_appbar(self):
        self.btn_logout = ft.IconButton(ft.icons.LOGOUT,tooltip="Cerrar sesión", visible=False)  
        appbar = ft.AppBar(
            leading=ft.Image(src="assets/icon.png", width=50, height=50),
            title=ft.Text("Ultitracking"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, 
                              tooltip="Cambiar tema", 
                              on_click=self.changed_theme),
                self.btn_logout
                    ]
                            )
        return appbar
    
    def changed_theme(self, e):
        # Cambiamos el tema a "light" si está en "dark", y viceversa
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        # Actualizamos la página una sola vez
        self.page.update()
        return True