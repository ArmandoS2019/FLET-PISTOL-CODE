import flet as ft
from components import (MyAppBar, MyCard, MyComponents, MyDataTable, 
                        BarcodeFrame, MyModal, MySnackBar, MyTheme,MyNavigationRail)

class Login2:
    
    def build(self, page: ft.Page):
        
        BarcodeFrame.__init__(self,page)