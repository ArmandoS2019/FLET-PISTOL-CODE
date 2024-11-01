import flet as ft


class MyNavigationRail:

    def __init__(self, page):
        self.page = page
        
    def my_navigation_rail(self, pick_files_dialog):
        
        rail = ft.NavigationRail(
            bgcolor=self.page.theme.color_scheme.primary_container,
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=ft.FloatingActionButton(icon=ft.icons.ADD_A_PHOTO, text="QR",
                                            on_click=lambda _: pick_files_dialog.pick_files(
                                            allow_multiple=True
                        )),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.IconButton(on_click=self.verify_check_true_datatable,
                                               icon=ft.icons.PICTURE_AS_PDF_ROUNDED),
                    label="Ver PDF",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.IconButton(on_click=self.btn_send_report_whatsapp,
                                               icon=ft.icons.SEND),
                    label="WhatsApp",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                    label_content=ft.Text("Settings"),
                ),
            ]
        )

        return ft.Row(
            [
                rail
            ]
        )   