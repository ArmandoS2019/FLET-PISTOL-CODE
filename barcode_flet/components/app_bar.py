import flet as ft


class MyAppBar:

    def __init__(self, page):
        self.page = page

    def create_appbar(self):
        self.btn_popup_change_theme = ft.PopupMenuItem(text='Cambiar modo',
                                    icon=ft.icons.WB_SUNNY_OUTLINED,
                                    on_click=self.changed_theme)
        
        btn_config = ft.PopupMenuButton(visible=True,
            items=[self.btn_popup_change_theme,
                   ft.PopupMenuItem(),
                   ft.PopupMenuItem(text='Editar perfil',
                                    icon=ft.icons.PERSON_2_ROUNDED, 
                                    on_click=self.logout),
                   ft.PopupMenuItem(),
                   ft.PopupMenuItem(text='Cerrar sesión',
                                    icon=ft.icons.LOGOUT, 
                                    on_click=self.logout)])
        
        row1 = ft.Row(controls=[ft.CircleAvatar(width=30, height=30,
                    foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"),
                    ft.Text('Armando.S.'),btn_config])
            
        self.btn_menu_profile = ft.Container(content=ft.Column(controls=[row1],
                                                               alignment=ft.MainAxisAlignment.CENTER))

        
        appbar = ft.AppBar(
            leading=ft.Image(src="assets/icon.png", width=50, height=50),leading_width=40,
            title=ft.Text("Ultitracking"),
            center_title=True,
            bgcolor=ft.colors.LIGHT_BLUE_900,
            actions=[self.btn_menu_profile])
        return appbar
    
    