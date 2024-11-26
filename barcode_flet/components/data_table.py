import flet as ft
from db.my_mongodb import collection_doc_data
import requests
from config.config import BASE_URL  # Import BASE_URL from config.py


class MyDataTable:

    def __init__(self, page):
        self.page = page
    
    def submit_pdf_report(self,e):
        try:
            # Realiza la solicitud GET
            response = requests.get(f"{BASE_URL}/reports/view-pdf")
            print(response)
            if response.status_code == 200:
                # results = response.json()
                # print(results)
                self.page.launch_url(f"{BASE_URL}/reports/view-pdf")
            else:
                print(f"Error al obtener datos: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error de solicitud: {e}")
            
    def verify_check_true_datatable(self, e):
        # Recopilar datos seleccionados
        selected_data = [
            row.cells[1].content.value  # Se obtiene el valor de la segunda celda
            for row in self.my_data_table.rows if row.selected is True
        ]
        
        # Procesar los datos seleccionados
        self.my_current_user = self.page.client_storage.get("username")
        self.my_image_report = self.get_image_report(selected_data, self.my_current_user)
        
        # Deseleccionar todas las filas después de la operación
        for row in self.my_data_table.rows:
            row.selected = False
        
        my_image_report = ft.Image(src_base64=self.my_image_report,
                               tooltip='Imprima su reporte',
                               filter_quality=ft.FilterQuality.LOW, 
                               width=300, 
                               height=None, 
                               fit=ft.ImageFit.CONTAIN,
                               border_radius=ft.border_radius.all(30))
        
        self.my_modal_show_report = self.modal_show_report(my_image_report)
        self.page.overlay.append(self.my_modal_show_report)
        self.my_modal_show_report.open = True
        self.page.update()
        return True
    
    def on_selection_change(self,e):
        print('-----')
        print(e)
        print('-----')
        e.control.selected = not e.control.selected  # Alternar entre seleccionado y no seleccionado
        e.page.update()  
        return True

    def insert_data_to_montodb(self):
        
        my_data = {'user_id':655,
                   'status_code':'Recibido en el archivo insp.',
                   'state':'DESPACHADO',
                   'date':'02-23-2024',
                   'updated_date':'09-03-2024'}
        
        result = collection_doc_data.insert_one(my_data).inserted_id 
        self.update_datatable()
        return result    
    
    def update_datatable(self):
        resultados = collection_doc_data.find().limit(50)
        my_rows = [ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(num))),
                ft.DataCell(ft.Text(str(documento.get("user_id", "")))),
                ft.DataCell(ft.Text(documento.get("status_code", ""))),
                ft.DataCell(ft.Text(documento.get("state", ""))),
                ft.DataCell(ft.Text(documento.get("date", ""))),
                ft.DataCell(ft.Text(documento.get("updated_date", ""))),],
            on_select_changed=self.on_selection_change) for num, documento in enumerate(resultados, start=1) ]
        
        # # Obtener los datos actualizados de MongoDB
        nuevos_datos = my_rows
        # # Actualizar las filas del DataTable con los nuevos datos
        self.my_data_table.rows = nuevos_datos
        # # Refrescar la página para mostrar los cambios
        self.page.update()
        return True
       
    def get_data_from_api(self):
        try:
            # Realiza la solicitud GET
            response = requests.get(f"{BASE_URL}/get_data/")
            if response.status_code == 200:
                results = response.json()
                # Construir filas para el DataTable
                my_rows = [
                    ft.DataRow(
    
                        cells=[
                            
                            ft.DataCell(ft.Text(str(num))),
                            ft.DataCell(ft.Text(item["user_id"])),
                            ft.DataCell(ft.Text(item["status_code"])),
                            ft.DataCell(ft.Text(item["state"])),
                            ft.DataCell(ft.Text(item["date"])),
                            ft.DataCell(ft.Text(item["updated_date"])),
                        ],
                        on_select_changed=self.on_selection_change
                    ) for num, item in enumerate(results['items'], start=1)
                ]
                return my_rows
            else:
                print(f"Error al obtener datos: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error de solicitud: {e}")
    
    def data_table(self):
        my_rows = self.get_data_from_api()
        my_column = [
                    ft.DataColumn(ft.Text("#")),
                    ft.DataColumn(ft.Text("Column 1"),on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
                    ft.DataColumn(ft.Text("Column 2")),
                    ft.DataColumn(ft.Text("Column 3")),
                    ft.DataColumn(ft.Text("Column 4")),
                    ft.DataColumn(ft.Text("Column 5"))
                    ]
        # Crear la tabla de datos (DataTable)
        self.my_data_table = ft.DataTable(expand=True,
                                          border=ft.border.all(2, "blue"), 
                                          border_radius=10,
                                          bgcolor=ft.colors.WHITE,
                                          vertical_lines=ft.BorderSide(1, "blue"),
                                          horizontal_lines=ft.BorderSide(1, "green"),
                                          heading_row_color=ft.colors.BLACK12,
                                          sort_column_index=0,
                                          sort_ascending=True,
                                          data_row_color={ft.ControlState.HOVERED: ft.colors.LIGHT_GREEN_ACCENT_100},
                                          show_checkbox_column=True,
                                          divider_thickness=0,
                                          heading_row_height=30,
                                          data_row_max_height=30,
                                          columns=my_column,
                                          rows=my_rows, 
                                          data_text_style = ft.TextStyle(
                                                color=self.page.theme.color_scheme.secondary,           # Color azul para el texto
                                                size=14,                         # Tamaño de fuente
                                                weight=ft.FontWeight.NORMAL,     # Peso de fuente normal (puede ser BOLD para negrita)
                                                font_family="Arial",             # Fuente específica
                                            ),
                                          heading_text_style=ft.TextStyle(
                                                color=self.page.theme.color_scheme.secondary,
                                                size=16,
                                                weight=ft.FontWeight.BOLD),
                                          )

        data_table_container = ft.Container(expand=True,
                                            width=1300, 
                                            alignment=ft.alignment.center,
                                            border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                            
                                            content=ft.Row(controls=[
                                                ft.Column(controls=[self.my_data_table],
                                                          auto_scroll=False, 
                                                          scroll=ft.ScrollMode.ALWAYS)],
                                                          scroll=ft.ScrollMode.ALWAYS)
                                            )
        return ft.Container(alignment=ft.alignment.center,
                            bgcolor=ft.colors.GREY_300,
                            content=ft.Column(controls=[data_table_container],
                                              alignment=ft.alignment.center))
    
