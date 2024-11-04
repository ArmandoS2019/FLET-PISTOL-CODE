import flet as ft
import time
from db.my_mongodb import collection
from components.data_table import DataTableApp
class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE       
        # Definir un diccionario con los atributos comunes
        self.common_attributes = {
            "expand":True,
            "border_radius": 10,
            'padding':2,
            "bgcolor":self.page.theme.color_scheme.secondary,
            }   
        
        self.barcode_input = ft.TextField(label="Escanea el código de barras aquí",
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_submit=self.on_submit_modal_status,
                                          keyboard_type=ft.KeyboardType.TEXT,
                                          bgcolor=ft.colors.LIGHT_BLUE_900, 
                                          text_style=ft.TextStyle(italic=True,
                                                                  bgcolor=ft.colors.INDIGO_900),
                                          label_style=ft.TextStyle(color=ft.colors.WHITE),
                                          color=ft.colors.YELLOW_ACCENT_200)
        
        self.my_card = self.my_card()
        self.data_table = self.data_table()
        
        self.row_barcode = ft.Row(
                            controls=[
                                ft.Container(**self.common_attributes,
                                    content=ft.Column(controls=[
                                        self.barcode_input]))
                                    ]
                                ) 
        self.column_cupertino_status_left = ft.Column(
                            controls=[
                                ft.Container(
                                    bgcolor=self.page.theme.color_scheme.primary,
                                    content=self.btn_cupertino_status())]
                                ) 
            
        self.table_container = ft.Container(**self.common_attributes,
                                            content=self.data_table)
        
        self.two_container_2 = ft.Row(expand=True,
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[self.table_container])
                
        
        self.barcode_container = ft.Row(spacing=10,
            expand=True,
            controls=[self.my_navigation_rail(),
                ft.Column(expand=True,
                          controls=[
                                    self.column_cupertino_status_left,
                                    self.row_barcode,
                                    self.two_container_2])
            ]
        )
        return self.barcode_container
                
