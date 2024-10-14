import flet as ft
import time

class BarcodeFrame:
    
    def __init__(self, page):
        self.page = page
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.title = "Ulti tracking"  
        self.page.window_favicon = ft.Image(src="assets/ulti.ico")

   
        my_appbar = self.create_appbar()
        self.barcode_input = ft.TextField(label="Escanea el código de barras aquí", 
                                          prefix_icon=ft.icons.QR_CODE_SCANNER,
                                          hint_text="Esperando lectura de codigo...", 
                                          on_change=self.on_change,
                                          keyboard_type=ft.KeyboardType.TEXT)
        self.resultado_text = ft.Text()
        self.my_card = self.my_card()
        self.data_table = self.data_table()

        my_container = ft.Row(
            [
            ft.Container(
                content=ft.Column(controls=[self.barcode_input,self.resultado_text,self.data_table]))],
            alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(my_appbar,my_container)
        
     # Función que simula un submit automático después de escribir
    def on_change(self,e):
        # Espera 1 segundo después de que el usuario deja de escribir
        time.sleep(5)
        self.on_enter(e)  # Llama al evento on_enter automáticamente

    # Función que se llama cuando el usuario presiona ENTER o el submit es automático
    def on_enter(self,e):
        self.dlg_modal = self.modal_alert_status()
        # self.resultado_text.value = f"Has escrito: {self.barcode_input.value}"
        if self.dlg_modal not in self.page.overlay:
            self.page.overlay.append(self.dlg_modal)
            self.dlg_modal.open = True
        else:
            self.dlg_modal.open = False
            self.page.update()
        self.page.update()
        return True
     
    def on_submit(self, e):
        self.dlg_modal = self.modal_alert_status()
        codigo = self.barcode_input.value
        if codigo == 'hola':
            if self.dlg_modal not in self.page.overlay:
                self.page.overlay.append(self.dlg_modal)
            self.dlg_modal.open = True
        else:
            self.dlg_modal.open = False
            self.page.update()
            # Mostramos el código escaneado en la pantalla
            self.resultado_text.value = f"Código no leído: {codigo}"
            # Limpiar el campo de texto para la siguiente lectura
            self.barcode_input.value = ""
            
        # Actualizamos la interfaz
        self.page.update()
        # Limpiar el campo de texto para la siguiente lectura
        self.barcode_input.value = ""
        return True
    
    def changed_theme(self, e):
        # Cambiamos el tema a "light" si está en "dark", y viceversa
        self.page.theme_mode = "light" if self.page.theme_mode == "dark" else "dark"
        # Actualizamos la página una sola vez
        self.page.update()
        return True
    
    def create_appbar(self):
        appbar = ft.AppBar(
            
            leading=ft.Image(src="assets/icon.png", width=40, height=40),
            leading_width=40,
            title=ft.Text("Ultitracking"),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            
            actions=[
                ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, 
                              tooltip="Cambiar tema", 
                              on_click=self.changed_theme),
                ft.IconButton(ft.icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # Divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, on_click='self.check_item_clicked'
                        ),
                    ]
                ),
            ],
        )
        return appbar

    def handle_close(self,e):
        self.page.close(self.dlg_modal)
        self.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
   
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
        actions=[self.my_card,
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: self.page.add(
            ft.Text("Modal dialog dismissed"),
        ),
        )
        return self.dlg_modal
     
    def data_table(self):
        
        # Función para manejar la selección de un checkbox en una fila
        def checkbox_fila_cambiado(e):
            seleccionadas = [fila.cells[0].content.value for fila in data_table.rows if fila.cells[0].content.value]
            estado_text = f"Filas seleccionadas: {', '.join([str(i) for i in seleccionadas])}"
            print("===========")
            print(e)
            print(estado_text)
            print("===========")
            self.page.update()
            
        # Datos originales
        data = [
            {"id": "1", "nombre": "Juan", "edad": "25"},
            {"id": "2", "nombre": "Ana", "edad": "30"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "3", "nombre": "Luis", "edad": "40"},
            {"id": "4", "nombre": "Carlos", "edad": "35"}
        ]
        rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Checkbox(on_change=checkbox_fila_cambiado)),
                    ft.DataCell(ft.Text(fila["nombre"])),
                    ft.DataCell(ft.Text(fila["edad"]))
                    ]) for fila in data]
                # on_select_changed=lambda e: print(f"row select changed: {e.data}")) for fila in data]
        
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
                    ft.DataColumn(ft.Text("Nombre")),
                    ft.DataColumn(ft.Text("Edad"))
                ],rows=rows)
        
        return data_table
    