import flet as ft
import threading
import time
from login.login import Login



def main(page: ft.Page):
    Login(page)
    

# Ejecutar la app Flet
ft.app(target=main, assets_dir="assets")