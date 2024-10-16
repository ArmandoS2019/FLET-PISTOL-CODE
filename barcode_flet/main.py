import flet as ft
import threading
import time
from core.core import MainApp



def main(page: ft.Page):
    MainApp(page)
    

# Ejecutar la app Flet
ft.app(target=main, assets_dir="assets")