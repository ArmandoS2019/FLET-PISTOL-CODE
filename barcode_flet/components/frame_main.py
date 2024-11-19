import flet as ft
import time
from db.my_mongodb import collection_doc_data
class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page
        
        
        self.my_snack_bar = self.get_snackbar()
        self.page.snack_bar = self.my_snack_bar
        
        self.dlg_modal = self.modal_alert_status()

        # Definir un diccionario con los atributos comunes
        self.common_attributes = {
            "expand":True,
            "border_radius": 10,
            'padding':2,
            }   
        
        self.btn_common_attributes = {
        "hover_color":ft.colors.YELLOW_200,
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
        self.barcode_input = ft.TextField(**self.btn_common_attributes,
                                          label="Escanea el código de barras aquí",
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_submit=self.on_submit_modal_status)
        
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
            
        self.table_container = ft.Container(padding=2, 
                                            expand=True,
                                            border_radius=3,  
                                            content=self.data_table)
        
        self.main_pagelet = ft.Pagelet(
                    expand=True,
                    appbar=self.create_appbar(),
                    content=ft.Container(padding=5,
                        content=ft.Column(
                          controls=[
                                    self.column_cupertino_status_left,
                                    self.barcode_input,
                                    self.table_container])),
                    bgcolor=ft.colors.WHITE,
                    bottom_app_bar=self.get_bottom_appbar(),
                    floating_action_button=self.get_floating_button(),
                    floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
                    
                )
        return self.main_pagelet
                
