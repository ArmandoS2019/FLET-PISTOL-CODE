import flet as ft

class MyTheme(ft.Page):
    
    def __init__(self, page):
        self.page = page
        
        # Definir el esquema de colores personalizado
        custom_theme = ft.Theme(
            
            color_scheme=ft.ColorScheme(
                primary=ft.colors.WHITE,
                secondary=ft.colors.BLUE_900,
                
                secondary_container=ft.colors.BLUE_GREY_50,
                
                on_error=ft.colors.RED_ACCENT_400,
                primary_container=ft.colors.SURFACE_VARIANT,
                on_tertiary_container=ft.colors.PRIMARY_CONTAINER,
                tertiary_container=ft.colors.BLACK12,
                on_tertiary=ft.colors.LIGHT_GREEN_ACCENT_700,
                tertiary=ft.colors.YELLOW_ACCENT_700,
                background="#04396b",  # Color de fondo de la página
                surface=ft.colors.LIGHT_BLUE_800,  # Color de fondo de los elementos superficiales
                on_primary=ft.colors.WHITE,  # Color para los textos en elementos primarios
                on_secondary=ft.colors.BLACK  # Color para textos en elementos secundarios
            ),
            
        scrollbar_theme=ft.ScrollbarTheme(
                track_color={
                    ft.MaterialState.HOVERED: ft.colors.BLUE_200,
                    ft.MaterialState.DEFAULT: ft.colors.PRIMARY_CONTAINER,
                },
                track_visibility=True,
                track_border_color=ft.colors.PRIMARY_CONTAINER,
                thumb_visibility=True,
                thickness=10,
                radius=5,
                main_axis_margin=5,
                cross_axis_margin=2,)
        )
        self.page.theme = custom_theme