import flet as ft
import shutil

class MyApp(ft.UserControl):
    def build(self):
        self.upload_message = ft.Text()
        self.file_picker = ft.FilePicker(on_result=self.upload_files_result)

        # Agregar el FilePicker al overlay de la página
        self.page.overlay.append(self.file_picker)

        return ft.Column([
            ft.ElevatedButton("Subir imagen", on_click=lambda _: self.file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)),
            self.upload_message
        ])

    def upload_files_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            print(e.files)
            # Obtener la ruta del archivo seleccionado
            file_path = e.files[0].path
            file_name = e.files[0].name
            print(file_path)
            print(file_name)
            # Guardar el archivo en una ubicación específica
            try:
                upload_path = f"uploads/{file_name}"
                with open(file_path, "rb") as src_file:
                    with open(upload_path, "wb") as dest_file:
                        shutil.copyfileobj(src_file, dest_file)

                self.upload_message.value = f"Imagen subida y guardada en: {upload_path}"
            except Exception as ex:
                self.upload_message.value = f"Error al subir la imagen: {ex}"

        else:
            self.upload_message.value = "No se seleccionó ningún archivo"

        self.upload_message.update()

def main(page: ft.Page):
    # Crear la carpeta de subidas si no existe
    import os
    if not os.path.exists('uploads'):
        os.makedirs('uploads')

    page.title = "Subir y Guardar Imagen"
    page.add(MyApp())

ft.app(target=main)
