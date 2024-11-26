import time
import flet as ft
import os
from components import (MyAppBar, 
                        MyCard, 
                        MyComponents, 
                        MyDataTable, 
                        BarcodeFrame, 
                        MyModal, 
                        MySnackBar, 
                        MyTheme, 
                        BottomAppBar, 
                        MyFloatinButton, 
                        MyNavigationDrawer, 
                        MyCupertinoActionSheet)
from report import MyReport
from config.config import BASE_URL  # Import BASE_URL from config.py
import requests 


class Login(MyTheme, MyAppBar,MyComponents,BarcodeFrame, MyReport, MyDataTable, MySnackBar,MyModal,MyCard,MyFloatinButton,BottomAppBar,MyNavigationDrawer, MyCupertinoActionSheet):
    
    def __init__(self, page):
        MyTheme.__init__(self,page)
        BarcodeFrame.__init__(self,page)
        MyReport.__init__(self)
        # Crear un Container que cubra toda la página y tenga una imagen de fondo
        self.background_container = ft.Container(
                    content=ft.Image(
                        width=self.page.width, 
                        height=self.page.height,
                        src="https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                        fit=ft.ImageFit.COVER
                        )
                    )
        
        
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 0  # Sin padding en la página
        self.page.spacing = 0  # Sin espacio entre widgets
        self.page.title = "Login"  
        self.page.assets_dir = os.path.join(os.getcwd(), "assets")
        self.page.window_favicon = ft.Image(src="ulti.ico")
        self.page.clean()
                   
        # self.page.add(self.main_pagelet) # FOR TEST
        self.btn_menu_profile.visible = True #this to be TRUE for test 
        self.page.on_login = self.my_login()
        
    def my_login(self):
        self.btn_common_attributes = {
        "keyboard_type":ft.KeyboardType.TEXT,
        "selection_color":ft.colors.LIGHT_BLUE_50,
        "border_radius": 10,
        'border_color':ft.colors.BLUE_100,                     # Color del borde del campo
        'focused_border_color':self.page.theme.color_scheme.secondary,             # Color del borde cuando está enfocado
        'cursor_color':self.page.theme.color_scheme.secondary,                     # Color del cursor (barra de texto)
        'bgcolor':ft.colors.GREY_100,
        'text_style':ft.TextStyle(color=ft.colors.BLUE_800),   # Color del texto de entrada
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
                #HERE Open SNACKBAR FOR gretting you
                self.page.snack_bar.open = True
                self.page.snack_bar.bgcolor = self.page.theme.color_scheme.tertiary
                self.page.snack_bar.content = self.my_card_snackbar('Bienvenido',
                                                                    'Ya estas en session',
                                                                    ft.icons.VERIFIED_USER)
                # self.page.update()  
                # self.page.add(ft.Stack(controls=[self.background_container,
                #                 ft.Container(content=self.main_pagelet,
                #                              padding=20,
                #                              alignment=ft.alignment.center)], 
                #      expand=True))
                self.page.add(self.main_pagelet)
                
            elif response.status_code == 401:
                #HERE Open SNACKBAR FOR ERROR user or pass
                self.page.snack_bar.open = True
                self.page.snack_bar.icon = ft.icons.PASSWORD
                self.page.snack_bar.bgcolor = self.page.theme.color_scheme.on_error
                self.page.snack_bar.content = self.my_card_snackbar('Usuario o contraseña incorrecto',
                                                                    'Vuelva a intentarlo',
                                                                    ft.icons.SECURITY)
                self.page.update()
                #H---------------------------
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
                
        user_session_text = ft.Text(value='Inicio Sesión de Usuario',
                                    size=20,
                                    color=ft.colors.WHITE,
                                    weight=ft.FontWeight.BOLD,
                                    font_family="Verdana",
                                    text_align=ft.TextAlign.CENTER,
                                    italic=True,
                                    opacity=0.8,
                                    max_lines=1) 
        
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
                                         bgcolor=self.page.theme.color_scheme.secondary,
                                         color=ft.colors.WHITE,
                                         icon=ft.icons.LOGIN, 
                                         on_click=authenticate_user)
        
                # Definir el contenedor de la imagen
        self.login_container = ft.Container(
            content=ft.Column(controls=[user_session_text,username_field,password_field,error_message,login_button],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=25,
            border_radius=10,  
            width=400,  # Ancho del contenedor
            height=300,
            bgcolor=None,
            
        )
        
                     
        # Agregar un contenedor principal para centrar todo el contenido en la pantalla
        self.page.add(
            ft.Stack(controls=[
                                self.background_container,
                                ft.Container(content=self.login_container,
                                             padding=20,
                                             alignment=ft.alignment.center),
                                ft.Container(content=ft.Text(value='Ulti-Tracking',
                                                             size=50, 
                                                             italic=True,
                                                             text_align=ft.TextAlign.CENTER),
                                             padding=100)
                                ], 
                     alignment=ft.alignment.top_center,
                     expand=True),
                )
        
    # Función para manejar el logout (cerrar sesión)
    def logout(self, e):
        self.btn_menu_profile.visible = False
        self.page.clean() 
        self.page.session.remove(self.page.client_storage.get("username"))
        self.page.add(
            ft.Stack(controls=[self.background_container,
                                ft.Container(content=self.login_container,
                                             padding=20,
                                             alignment=ft.alignment.center)], 
                     expand=True),
                )
        