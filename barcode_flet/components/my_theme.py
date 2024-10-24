import flet as ft

class MyTheme(ft.Page):
    
    def __init__(self, page):
        self.page = page
        
        # Definir el esquema de colores personalizado
        custom_theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary_container=ft.colors.SURFACE_VARIANT,
                secondary_container=ft.colors.BLUE_GREY_700,
                tertiary_container=ft.colors.BLACK12,
                primary=ft.colors.BLUE,
                secondary=ft.colors.LIGHT_GREEN_ACCENT_400,
                on_tertiary=ft.colors.LIGHT_GREEN_ACCENT_700,
                tertiary=ft.colors.YELLOW_ACCENT_700,
                on_error=ft.colors.RED_ACCENT_400,
                background=ft.colors.GREY_200,  # Color de fondo de la página
                surface=ft.colors.GREY_50,  # Color de fondo de los elementos superficiales
                on_primary=ft.colors.WHITE,  # Color para los textos en elementos primarios
                on_secondary=ft.colors.BLACK  # Color para textos en elementos secundarios
            ),
        )
        self.page.theme = custom_theme