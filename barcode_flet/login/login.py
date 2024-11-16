import time
import flet as ft
import os
from components import (MyAppBar, MyCard, MyComponents, MyDataTable, 
                        BarcodeFrame, MyModal, MySnackBar, MyTheme,MyNavigationRail)
from report import MyReport
from config.config import BASE_URL  # Import BASE_URL from config.py
import requests 


class Login(MyTheme, MyAppBar,MyComponents,BarcodeFrame, MyReport,MyDataTable, MySnackBar,MyModal,MyCard,MyNavigationRail):
    
    def __init__(self, page):
        MyTheme.__init__(self,page)
        BarcodeFrame.__init__(self,page)
        MyReport.__init__(self)

        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 0  # Sin padding en la página
        self.page.spacing = 0  # Sin espacio entre widgets
        self.page.bgcolor = ft.colors.WHITE
        self.page.title = "Login"  
        self.page.assets_dir = os.path.join(os.getcwd(), "assets")
        self.page.window_favicon = ft.Image(src="ulti.ico")
        # self.page.theme_mode = ft.ThemeMode.DARK
        self.page.appbar = self.create_appbar()
        self.page.clean()
        self.page.add(self.barcode_container) # FOR TEST
        self.btn_menu_profile.visible = True #this to be TRUE for test 
        # self.page.on_login = self.my_login()
        
    def my_login(self):
        self.btn_common_attributes = {
        "keyboard_type":ft.KeyboardType.TEXT,
        "selection_color":ft.colors.LIGHT_BLUE_50,
        "border_radius": 10,
        'border_color':ft.colors.BLUE_100,                     # Color del borde del campo
        'focused_border_color':ft.colors.BLUE_900,             # Color del borde cuando está enfocado
        'cursor_color':ft.colors.BLUE_900,                     # Color del cursor (barra de texto)
        'bgcolor':ft.colors.GREY_100,
        'text_style':ft.TextStyle(color=ft.colors.BLUE_900),   # Color del texto de entrada
        'label_style':ft.TextStyle(color=ft.colors.BLUE_800),  # Color de la etiqueta (label)
        'hint_style':ft.TextStyle(color=ft.colors.BLUE_GREY_600),                 # Ícono de sufijo
        }  
        
        def authenticate_user(e):
            username = username_field.value
            password = password_field.value
            
            data = {
            "username": username_field.value,
            "password": password_field.value}

            response = requests.post(BASE_URL+'/login/', json=data)
            
            if  response.status_code == 200:
                self.page.session.set(username, True)  # Establecer la sesión como autenticada
                self.page.client_storage.set("username", username)
                self.page.clean()  # Limpiar la página
                self.btn_menu_profile.visible = True #If you are logged in INVISIBLE TRUE, else FALSE 
                username_field.value = ""
                password_field.value = ""
                error_message.value = ""
                self.page.add(self.barcode_container,ft.SnackBar(ft.Text(response.json()["msg"]), open=True))
                # self.page.add(ft.SnackBar(ft.Text(response.json()["msg"]), open=True))
            elif response.status_code == 401:
                error_message.value = "Usuario o contraseña incorrecto."
                username_field.value = ""
                password_field.value = ""
                username_field.update()
                password_field.update()
                error_message.update()
            elif username_field.value == "" and password_field.value == "":
                error_message.value = ""
                error_message.update()  

        # Campos del formulario de login
                
        user_session_text = ft.Text(value='Inicio de Sesión de Usuario', 
                                    size=18, 
                                    color=ft.colors.BLUE_900, 
                                    italic=True) 
        
        error_message = ft.Text(color=self.page.theme.color_scheme.on_error)  # Texto para mensajes de error
        
        username_field = ft.TextField(**self.btn_common_attributes,
                                      label="Usuario",
                                      suffix_icon=ft.icons.PERSON_2_OUTLINED,
                                      autofocus=True,
                                      hint_text='Escriba su usuario')
        password_field = ft.TextField(**self.btn_common_attributes,
                                      label="Contraseña",
                                      suffix_icon=ft.icons.LOCK, 
                                      password=True,
                                      can_reveal_password=True,
                                      hint_text='Escriba su contraseña')
    
       
        # Botón de iniciar sesión
        login_button = ft.ElevatedButton("Iniciar sesión",
                                         bgcolor=ft.colors.BLUE_900,
                                         color=ft.colors.WHITE,
                                         icon=ft.icons.LOGIN, 
                                         on_click=authenticate_user)
        
                # Definir el contenedor de la imagen
        self.login_container = ft.Container(
            content=ft.Column(
                controls=[user_session_text,username_field,password_field,error_message,login_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=25,
            border_radius=0,  
            width=400,  # Ancho del contenedor
            height=300,
            bgcolor=ft.colors.GREY_200,
            shadow=ft.BoxShadow(
            spread_radius=1,        # Expande el área de la sombra
            blur_radius=15,         # Nivel de desenfoque de la sombra
            color=ft.colors.BLUE_300,  # Color de la sombra en RGBA para transparencia
            offset=ft.Offset(5, 5)  # Posición de la sombra (x, y)
        )
        )
        
        # Agregar un contenedor principal para centrar todo el contenido en la pantalla
        self.page.add(
            ft.Container(
                content=self.login_container, alignment=ft.alignment.center, expand=True))
        
    # Función para manejar el logout (cerrar sesión)
    def logout(self, e):
        self.btn_menu_profile.visible = False
        self.page.clean() 
        self.page.session.remove(self.page.client_storage.get("username"))
        self.page.add(ft.Container(content=self.login_container, alignment=ft.alignment.center, expand=True))
        