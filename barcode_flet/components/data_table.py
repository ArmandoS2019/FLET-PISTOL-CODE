import flet as ft
from db.my_mongodb import collection

class MyDataTable:

    def __init__(self, page):
        self.page = page

    def verify_check_true_datatable(self, e):
        # Recopilar datos seleccionados
        selected_data = [
            row.cells[1].content.value  # Se obtiene el valor de la segunda celda
            for row in self.my_data_table.rows if row.selected is True
        ]
        
        # Procesar los datos seleccionados
        self.my_current_user = self.page.client_storage.get("username").lower()
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
        e.control.selected = not e.control.selected  # Alternar entre seleccionado y no seleccionado
        e.page.update()  
        return True

    def insert_data_to_montodb(self):
        my_data = {'user_id':655,
                   'status_code':'Recibido en el archivo insp.',
                   'state':'DESPACHADO',
                   'date':'02-23-2024',
                   'updated_date':'09-03-2024'}
        
        result = collection.insert_one(my_data).inserted_id 
        self.update_datatable()
        return result    
    
    def update_datatable(self):
        resultados = collection.find().limit(50)
        my_rows = [ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(num))),
                ft.DataCell(ft.Text(str(documento.get("user_id", "")))),
                ft.DataCell(ft.Text(documento.get("status_code", ""))),
                ft.DataCell(ft.Text(documento.get("state", ""))),
                ft.DataCell(ft.Text(documento.get("date", ""))),
                ft.DataCell(ft.Text(documento.get("updated_date", ""))),],
            on_select_changed=self.on_selection_change) for num, documento in enumerate(resultados, start=1) ]
        
        # Obtener los datos actualizados de MongoDB
        nuevos_datos = my_rows
        # Actualizar las filas del DataTable con los nuevos datos
        self.my_data_table.rows = nuevos_datos
        # Refrescar la página para mostrar los cambios
        self.page.update()
        return True
     
    def data_table(self):
        
        my_column = [ft.DataColumn(ft.Text("#")),
                    ft.DataColumn(ft.Text("Column 1"),on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
                    ft.DataColumn(ft.Text("Column 2")),
                    ft.DataColumn(ft.Text("Column 3")),
                    ft.DataColumn(ft.Text("Column 4")),
                    ft.DataColumn(ft.Text("Column 5"))
                    ]

        # Crear filas dinámicas desde los resultados de MongoDB
        resultados = collection.find().limit(50)
        my_rows = [ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(num))),
                ft.DataCell(ft.Text(str(documento.get("user_id", "")))),
                ft.DataCell(ft.Text(documento.get("status_code", ""))),
                ft.DataCell(ft.Text(documento.get("state", ""))),
                ft.DataCell(ft.Text(documento.get("date", ""))),
                ft.DataCell(ft.Text(documento.get("updated_date", ""))),
            ],
            on_select_changed=self.on_selection_change) for num, documento in enumerate(resultados, start=1) ]

        # Crear la tabla de datos (DataTable)
        self.my_data_table = ft.DataTable(expand=True,show_checkbox_column=True,
                                            heading_row_height=30,
                                            data_row_max_height=30,
                                            columns=my_column,
                                            rows=my_rows)
        
        data_table_container = ft.Container(expand=True,
                                            border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                            shadow=ft.BoxShadow(spread_radius=8,
                                                                blur_radius=15,
                                                                color=ft.colors.with_opacity(0.15,'black')),
                                            bgcolor=self.page.theme.color_scheme.primary_container,
                                            content=ft.Row(controls=[ft.Column(controls=[self.my_data_table],
                                                                auto_scroll=False, 
                                                                scroll=ft.ScrollMode.ALWAYS)],
                                                           scroll=ft.ScrollMode.ALWAYS)
                                            )
        return data_table_container