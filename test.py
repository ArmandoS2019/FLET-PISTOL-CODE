import flet as ft

# Definir función para deseleccionar todos los checkboxes
def deseleccionar_todos(e):
    # Iterar sobre todas las filas de la tabla
    for row in datatable.rows:
        # Cambiar el estado del checkbox a False (deseleccionado)
        row.cells[0].content.value = False  # content es el checkbox en la primera columna
    e.page.update()  # Actualizar la página para reflejar los cambios

# Definir DataTable con checkboxes
datatable = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Seleccionar")),
        ft.DataColumn(ft.Text("Nombre")),
        ft.DataColumn(ft.Text("Edad")),
    ],
    rows=[
        ft.DataRow(cells=[
            ft.DataCell(ft.Checkbox(value=True)),  # Inicialmente seleccionado
            ft.DataCell(ft.Text("Juan Perez")),
            ft.DataCell(ft.Text("30")),
        ]),
        ft.DataRow(cells=[
            ft.DataCell(ft.Checkbox(value=True)),  # Inicialmente seleccionado
            ft.DataCell(ft.Text("Maria Gomez")),
            ft.DataCell(ft.Text("25")),
        ]),
        ft.DataRow(cells=[
            ft.DataCell(ft.Checkbox(value=True)),  # Inicialmente seleccionado
            ft.DataCell(ft.Text("Carlos Ruiz")),
            ft.DataCell(ft.Text("35")),
        ]),
    ],
)

# Definir la página principal
def main(page: ft.Page):
    # Botón para deseleccionar todos los checkboxes
    deseleccionar_btn = ft.ElevatedButton("Deseleccionar Todos", on_click=deseleccionar_todos)

    # Agregar el DataTable y el botón a la página
    page.add(datatable, deseleccionar_btn)

# Ejecutar la app Flet
ft.app(target=main)
