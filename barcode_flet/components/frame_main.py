import flet as ft
import time

class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page
        
        # Definir un diccionario con los atributos comunes
        self.common_attributes = {
            "expand": True,
            "border_radius": 10
        }
                
        self.barcode_input = ft.TextField(label="Escanea el código de barras aquí", 
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_submit=self.on_submit_modal_status,
                                          keyboard_type=ft.KeyboardType.TEXT)
        
        # self.resultado_text = ft.Text()
        self.my_card = self.my_card()
        self.data_table = self.data_table()
        
        self.top_barcode_container = ft.Container(
                                    bgcolor=self.page.theme.color_scheme.primary_container,
                                    expand=False,
                                    border_radius=10,
                                    height=60, 
                                    content=ft.Column(controls=[self.barcode_input],
                                                      alignment=ft.MainAxisAlignment.CENTER))
        
        self.table_container = ft.Container(bgcolor=self.page.theme.color_scheme.primary_container,
                                            **self.common_attributes,
                                            content=self.data_table)
        
        # Crear una columna con dos contenedores, uno encima del otro
        self.column_status_left = ft.Column(
                                    expand=True,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.START,  # Alinear en la parte superior
                                    controls=[
                                        ft.Container(
                                            bgcolor=self.page.theme.color_scheme.primary_container,
                                            expand=False,
                                            margin=10,
                                            border_radius=5,
                                            content=ft.Text("Aquí muestro tu estatus seleccionado"),
                                        ),
                                        ft.Container(
                                            bgcolor=self.page.theme.color_scheme.tertiary_container,
                                            content=self.btn_cupertino_status(),  # Segundo contenedor con un botón u otro contenido
                                            padding=20,
                                            margin=10,
                                            border_radius=10,
                                        )
                                    ]
                                )          
        
        self.column_whatsapp_center = ft.Column(
                                    expand=True,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.START,  # Alinear en la parte superior
                                    controls=[ft.ElevatedButton(text='WhatsApp',
                                                                        on_click=self.btn_send_report_whatsapp,
                                                                        icon=ft.icons.SEND_AND_ARCHIVE_ROUNDED)
                                    ]
                                )          
                                                                        
        self.column_report_right = ft.Column(
                                    expand=True,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.START,  # Alinear en la parte superior
                                    controls=[
                                        ft.Container(
                                            bgcolor=self.page.theme.color_scheme.primary_container,
                                            expand=False,
                                            margin=10,
                                            border_radius=5,
                                            content=ft.Text("Imprima un recibo o envilo por WhatsApp"),
                                        ),
                                        ft.Container(
                                            content=ft.Row(
                                            [
                                                ft.ElevatedButton(text='PDF', 
                                                                      on_click=self.verify_check_true_datatable,
                                                                      icon=ft.icons.PICTURE_AS_PDF_ROUNDED),
                                                
                                            ]),  # Segundo contenedor con un botón u otro contenido
                                            padding=20,
                                            margin=10,
                                            border_radius=10,
                                            bgcolor=self.page.theme.color_scheme.primary_container
                                        )
                                    ]
                                )          
                                                                        
        self.container_status = ft.Container(**self.common_attributes, bgcolor=self.page.theme.color_scheme.primary_container,
                                            content=self.column_status_left)

        self.container_report = ft.Container(**self.common_attributes, bgcolor=self.page.theme.color_scheme.primary_container,
                                             content=self.column_report_right)
            
        self.container_whatsapp_report = ft.Container(**self.common_attributes, bgcolor=self.page.theme.color_scheme.primary_container,
                                             content=self.column_whatsapp_center)
            
            
        self.frame_stadistic = ft.Container(bgcolor=self.page.theme.color_scheme.primary_container,
                                            **self.common_attributes)
        
        
        self.two_container = ft.Row(controls=[self.container_status,self.container_report,self.container_whatsapp_report])
        
        self.barcode_container = ft.Row(
            expand=True,
            controls=[
                self.table_container,
                ft.Column(expand=True,
                          controls=[self.two_container,self.frame_stadistic]),
                
            ]
        )
        self.page.add(self.top_barcode_container)
                
