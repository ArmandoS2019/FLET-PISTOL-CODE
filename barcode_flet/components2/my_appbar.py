import flet as ft

class MyAppBar(ft.AppBar):
    def __init__(self, title_text: str):
        
        self.btn_popup_change_theme = ft.PopupMenuItem(text='Cambiar modo',
                                    icon=ft.icons.WB_SUNNY_OUTLINED,
                                    on_click='self.changed_theme')
        
        btn_config = ft.PopupMenuButton(visible=True,
                                        bgcolor=ft.colors.BLUE_800,
                                        icon_color=ft.colors.WHITE,
            items=[self.btn_popup_change_theme,
                   ft.PopupMenuItem(),
                   ft.PopupMenuItem(text='Editar perfil',
                                    icon=ft.icons.PERSON_2_ROUNDED, 
                                    on_click='self.logout'),
                   ft.PopupMenuItem(),
                   ft.PopupMenuItem(text='Cerrar sesión',
                                    icon=ft.icons.LOGOUT, 
                                    on_click='self.logout')])
        
        row1 = ft.Row(controls=[ft.CircleAvatar(width=30, height=30,
                    foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"),
                    ft.Text(value='hola')])
            
        btn_menu_profile = ft.Container(content=ft.Column(controls=[row1],
                                                               alignment=ft.MainAxisAlignment.CENTER))
                
        
        super().__init__(
            title=ft.Text(title_text),
            bgcolor=ft.colors.BLUE,
            center_title=True,
            leading=ft.Icon(ft.icons.MENU),
            actions=[btn_menu_profile,btn_config]
        )