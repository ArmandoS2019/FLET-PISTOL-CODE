import flet as ft
import time
from components.components import BarcodeFrame
from components.app_bar import AppBar


class Login(AppBar,BarcodeFrame):
    
    def __init__(self, page):
        BarcodeFrame.__init__(self,page)
        self.page = page
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.title = "Login"  
        self.page.window_favicon = ft.Image(src="assets/ulti.ico")
        self.page.appbar = self.create_appbar()
        
        # self.page.add(self.barcode_container)
        
        def authenticate_user(e):
            username = username_field.value
            password = password_field.value
            # Validar credenciales (por simplicidad se usa un ejemplo fijo)
            if username == "a" and password == "1":
                self.page.session.set("logged_in", True)  # Establecer la sesión como autenticada
                self.page.clean()  # Limpiar la página
                self.btn_logout.visible = True 
                self.page.add(self.barcode_container)
            else:
                error_message.value = "Usuario o contraseña incorrectos."
                error_message.update()

        # Campos del formulario de login
        username_field = ft.TextField(label="Usuario", autofocus=True)
        password_field = ft.TextField(label="Contraseña", password=True)
        
        error_message = ft.Text(color=ft.colors.RED)  # Texto para mensajes de error
        
        # Botón de iniciar sesión
        login_button = ft.ElevatedButton("Iniciar sesión", on_click=authenticate_user)
        
        # Agregar el formulario de login a la página
        login_container=ft.Container(ft.Column(
                                        controls=[username_field, password_field, error_message, login_button],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=20,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=50,
                            border_radius=10,  
                            alignment=ft.alignment.center,  # Centrar el contenedor
                            width=400,  # Ancho del contenedor
                            height=300)
        
        self.page.add(ft.Container(content=login_container, alignment=ft.alignment.center, expand=True))