import flet as ft
import time

class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page
        
                
        def pick_files_result(e: ft.FilePickerResultEvent): 
            selected_files.value = ( ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!" ) 
            selected_files.update()
        
        # Definir un diccionario con los atributos comunes
        self.common_attributes = {
            "expand":True,
            "border_radius": 10,
            'padding':20,
            "bgcolor":self.page.theme.color_scheme.primary_container
            }
        
        def pick_files_result(e: ft.FilePickerResultEvent):
                selected_files.value = (
                    ", ".join(map(lambda f: f.name, e.files)) if e.files else "No selecciono!"
                )
                selected_files.update()

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()

        self.page.overlay.append(pick_files_dialog)

        self.mypicker=ft.Row(
                [
                    ft.ElevatedButton(
                        "Suba una \nfoto QR",
                        icon=ft.icons.ADD_A_PHOTO,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),
                    selected_files,
                ]
            )   
            
        self.barcode_input = ft.TextField(label="Escanea el código de barras aquí",
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_submit=self.on_submit_modal_status,
                                          keyboard_type=ft.KeyboardType.TEXT,
                                          adaptive=True)
        
        self.my_card = self.my_card()
        self.data_table = self.data_table()
        
        self.row_barcode = ft.Row(height=140,
                            controls=[
                                ft.Container(**self.common_attributes,
                                    content=ft.Column(controls=[
                                        self.barcode_input,
                                        self.mypicker]))
                                    ]
                                ) 
        self.column_cupertino_status_left = ft.Column(
                            controls=[
                                ft.Container(
                                    bgcolor=self.page.theme.color_scheme.tertiary_container,
                                    content=self.btn_cupertino_status())]
                                ) 
            
        self.table_container = ft.Container(**self.common_attributes,
                                            content=self.data_table)
        
        self.two_container_2 = ft.Row(expand=True,
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[self.table_container])
                
        
        self.barcode_container = ft.Row(
            expand=True,
            controls=[self.my_navigation_rail(pick_files_dialog),
                ft.Column(expand=True,
                          controls=[
                                    self.column_cupertino_status_left,
                                    self.row_barcode,
                                    self.two_container_2])
            ]
        )
        return self.barcode_container
                
