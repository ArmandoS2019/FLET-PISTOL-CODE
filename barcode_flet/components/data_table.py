import flet as ft
from db.my_mongodb import collection

class MyDataTable:

    def __init__(self, page):
        self.page = page

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
        self.my_data_table = ft.DataTable(show_checkbox_column=True,
                                            on_select_all=False,
                                            width=380,
                                            heading_row_height=40,
                                            data_row_max_height=40,
                                            columns=my_column,
                                            rows=my_rows)
        
        data_table_container = ft.Container(expand=True,
                                            width=600,
                                            padding=10,
                                            border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                            shadow=ft.BoxShadow(spread_radius=8,
                                                                blur_radius=15,
                                                                color=ft.colors.with_opacity(0.15,'black')),
                                            bgcolor=self.page.theme.color_scheme.primary_container,
                                            content=ft.Column(controls=[self.my_data_table],
                                                                auto_scroll=False, 
                                                                scroll=ft.ScrollMode.ALWAYS,
                                                                height=800)
                                            )
        # # ,
        
        return data_table_container