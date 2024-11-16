import flet as ft
from components2.my_appbar import MyAppBar
from login.login import Login

class HomePage:
    
    def build(self, page: ft.Page):
        Login(page)