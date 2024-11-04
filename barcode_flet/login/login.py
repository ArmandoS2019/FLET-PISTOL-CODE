import time
import flet as ft
from components import (MyAppBar, MyCard, MyComponents, MyDataTable, 
                        BarcodeFrame, MyModal, MySnackBar, MyTheme,MyNavigationRail)
from report import MyReport

class Login(MyTheme, MyAppBar,MyComponents,BarcodeFrame, MyReport,MyDataTable, MySnackBar,MyModal,MyCard,MyNavigationRail):
    
    def __init__(self, page):
        MyTheme.__init__(self,page)
        BarcodeFrame.__init__(self,page)
        MyReport.__init__(self)

        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 0  # Sin padding en la página
        self.page.spacing = 0  # Sin espacio entre widgets
        # self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.title = "Login"  
        self.page.window_favicon = ft.Image(src="assets/ulti.ico")
        # self.page.theme_mode = ft.ThemeMode.DARK
        self.page.appbar = self.create_appbar()
        self.page.clean()
        self.page.add(self.barcode_container) # FOR TEST
        self.btn_menu_profile.visible = True #this to be TRUE for test 
        # self.page.on_login = self.my_login()
        
    def my_login(self):
        
        def authenticate_user(e):
            username = username_field.value
            password = password_field.value
            # Validar credenciales (por simplicidad se usa un ejemplo fijo)
            if username == "a" and password == "1":
                self.page.session.set(username, True)  # Establecer la sesión como autenticada
                self.page.client_storage.set("username", username)
                
                self.page.clean()  # Limpiar la página
                self.btn_menu_profile.visible = True #If you are logged in INVISIBLE TRUE, else FALSE 
                username_field.value = ""
                password_field.value = ""
                error_message.value = ""
                self.page.add(self.barcode_container)
            else:
                error_message.value = "Usuario o contraseña incorrectos."
                error_message.update()

        # Campos del formulario de login
        username_field = ft.TextField(label="Usuario", autofocus=True)
        password_field = ft.TextField(label="Contraseña", 
                                      password=True,
                                      can_reveal_password=True)
        
        error_message = ft.Text(color=self.page.theme.color_scheme.on_error)  # Texto para mensajes de error
       
        # Botón de iniciar sesión
        login_button = ft.ElevatedButton("Iniciar sesión",
                                         icon=ft.icons.LOGIN, 
                                         on_click=authenticate_user)
        
        # Agregar el formulario de login a la página
        self.login_container=ft.Container(ft.Column(
                                        controls=[username_field, password_field, error_message, login_button],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=5,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                            padding=50,
                            border_radius=10,  
                            alignment=ft.alignment.center,  # Centrar el contenedor
                            width=400,  # Ancho del contenedor
                            height=300)
        
        self.page.add(ft.Container(content=self.login_container, alignment=ft.alignment.center, expand=True))
        
    # Función para manejar el logout (cerrar sesión)
    def logout(self, e):
        self.btn_menu_profile.visible = False
        self.page.clean() 
        self.page.session.remove(self.page.client_storage.get("username"))
        self.page.add(ft.Container(content=self.login_container, alignment=ft.alignment.center, expand=True))
        