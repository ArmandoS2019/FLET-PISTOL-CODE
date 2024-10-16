import flet as ft
import time


class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page

        self.barcode_input = ft.TextField(label="Escanea el código de barras aquí", 
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_submit=self.on_submit,
                                          keyboard_type=ft.KeyboardType.TEXT)
        
        self.resultado_text = ft.Text()
        self.my_card = self.my_card()
        self.data_table = self.data_table()

        self.barcode_container = ft.Container(
                                    content=ft.Column(
                                                controls=[self.barcode_input,
                                                          self.resultado_text,
                                                          self.data_table]))
            
            
            
        self.barcode_container = ft.Row(
            [
            ft.Container(
                content=ft.Column(controls=
                                  [self.barcode_input,self.resultado_text,self.data_table]))],
            alignment=ft.MainAxisAlignment.CENTER)
    
    
    def on_submit(self, e):
        self.dlg_modal = self.modal_alert_status()
        codigo = self.barcode_input.value
        if codigo == 'a':
            self.dlg_modal = self.modal_alert_status()
            self.page.overlay.append(self.dlg_modal)
            self.dlg_modal.open = True
            self.page.update()
        else:
            self.dlg_modal.open = False
            self.page.update()
            # Limpiar el campo de texto para la siguiente lectura
            self.barcode_input.value = ""
        # Actualizamos la interfaz
        self.page.update()
        return True
    
   
    
    def handle_close(self,e):
        self.page.close(self.dlg_modal)
        self.page.update()
        self.barcode_input.focus()
        self.barcode_input.value=''
        return True
   
    def my_card(self):
        self.mycard = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DESCRIPTION),
                            title=ft.Text("The Enchanted Nightingale"),
                            subtitle=ft.Text(
                                "Music by Julie Gable. Lyrics by Sidney Stein."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Recibir", on_click=self.handle_close, 
                                icon=ft.icons.CHECK_CIRCLE,
                                icon_color=ft.colors.GREEN, 
                                style=ft.ButtonStyle(color=ft.colors.GREEN)), 
                             ft.TextButton("Rechazar", on_click=self.handle_close, 
                                icon=ft.icons.CANCEL,  
                                icon_color=ft.colors.RED,
                                style=ft.ButtonStyle(color=ft.colors.RED))],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        return self.mycard
        
    def modal_alert_status(self):
        self.dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[self.my_card],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: self.page.add(ft.Text("Modal dialog dismissed")),
        )
        return self.dlg_modal
     
    def data_table(self):
        # Función para manejar la selección de un checkbox en una fila
        def checkbox_fila_cambiado(e):
            seleccionadas = [fila.cells[0].content.value for fila in data_table.rows if fila.cells[0].content.value]
            estado_text = f"Filas seleccionadas: {', '.join([str(i) for i in seleccionadas])}"
            self.page.update()
        
        def on_button_click(e):
            selected_row = e.control.data
            self.page.snack_bar = ft.SnackBar(ft.Text(f"Botón en la fila {selected_row} presionado"))
            self.page.snack_bar.open = True
            self.page.update()
        
        # Datos originales
        data = [
            {"id": "counter",
             "btn": "d", 
             "check": "1",
             "nombre": "Juan", 
             "edad": "25"},
            {"id": "counter",
             "btn": "d", 
             "check": "1",
             "nombre": "Juan", 
             "edad": "25"},
            {"id": "counter",
             "btn": "d", 
             "check": "1",
             "nombre": "Juan", 
             "edad": "25"},
            {"id": "counter",
             "btn": "d", 
             "check": "1",
             "nombre": "Juan", 
             "edad": "25"},
     
        ]
        rows = [
            ft.DataRow(
                cells=[
                    
                    ft.DataCell(ft.Text(f"{count + 1}")),
                    ft.DataCell(ft.Text(fila["btn"])),
                    ft.DataCell(ft.Text(fila["check"])),
                    ft.DataCell(ft.Text(fila["nombre"])),
                    ft.DataCell(ft.Text(fila["edad"]))
                    ]) for count,fila in enumerate(data, start=0)]
                # on_select_changed=lambda e: print(f"row select changed: {e.data}")) for fila in data]
        # ft.DataCell(ft.ElevatedButton("Acción",on_click=on_button_click)),
        #             ft.DataCell(ft.Checkbox(on_change=checkbox_fila_cambiado)),
        # Crear la tabla de datos (DataTable)
        data_table = ft.DataTable(
            border=ft.border.all(2, "red"),
            border_radius=10,
            vertical_lines=ft.BorderSide(3, "blue"),
            horizontal_lines=ft.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            show_checkbox_column=True,show_bottom_border=True,
            divider_thickness=0,
            column_spacing=200,
            expand=True,    
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("btn")),
                    ft.DataColumn(ft.Text("check")),
                    ft.DataColumn(ft.Text("Nombre")),
                    ft.DataColumn(ft.Text("Edad"))
                ],rows=rows)
        
        return data_table
    