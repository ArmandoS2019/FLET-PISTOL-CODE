import flet as ft

def main(page: ft.Page):
    # Crear un CircleAvatar con un estilo moderno
    avatar_moderno = ft.CircleAvatar(
        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",  # Imagen de perfil
        radius=50,  # Tamaño del avatar
        bgcolor=ft.colors.BLUE_GREY_900,  
        width=3
    )
    
    # Crear un contenedor para centrar el avatar
    container = ft.Container(
        content=avatar_moderno,
        alignment=ft.alignment.center,  # Centrar el avatar
        padding=20
    )
    
    # Agregar el contenedor a la página
    page.add(container)

# Ejecutar la aplicación
ft.app(target=main)
