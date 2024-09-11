import flet as ft


class Patients(ft.Column):

    def __init__(self, patients_list):

        self.patients_list = patients_list
        self.add_patient = ft.FloatingActionButton(
            text="Add a new patient",
            icon=ft.icons.ADD,
        )
        self.searchbar = ft.SearchBar(
            bar_leading=ft.Icon(ft.icons.SEARCH),
            view_elevation=4,
            # divider_color=ft.colors.AMBER,
            bar_hint_text="Search patients...",
            view_hint_text="Choose a patient from the list...",
            on_change=self._handle_change,
            on_submit=self._handle_submit,
            on_tap=self._handle_tap,
            controls=[
                # ft.AutoComplete(
                #     suggestions=[
                #         ft.AutoCompleteSuggestion(key=f"{patient}", value=f"{patient}")
                #         for patient in self.patients_list
                #     ],
                #     on_select=self._close_anchor,
                # ),
                ft.ListTile(
                    title=ft.Text(f"{patient}"),
                    on_click=self._close_anchor,
                    data=patient,
                )
                for patient in self.patients_list
            ],
        )

        self.patient_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON),
                            title=ft.Text("NAME - LAST NAME"),
                            subtitle=ft.Text("LAST VISITED ON "),
                        ),
                        ft.Row(
                            [
                                ft.TextButton("Edit information"),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_FOREVER,
                                    icon_color=ft.colors.RED_500,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            ),
            elevation=3,
        )

        self.grid_patients = ft.GridView(
            expand=True,
            # runs_count=5,
            max_extent=500,
            child_aspect_ratio=2.8,
            spacing=5,
            run_spacing=5,
            controls=[self.patient_card for _ in self.patients_list],
        )

        super(Patients, self).__init__(
            controls=[self.searchbar, self.grid_patients, self.add_patient],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=40,
            visible=False,
        )

    def _close_anchor(self, e):
        self.searchbar.close_view(f"Patient {e.control.data}")

    def _handle_change(self, e):
        # TODO Implement search here
        print(f"handle_change e.data: {e.data}")

    def _handle_submit(self, e):
        print(f"handle_submit e.data: {e.data}")

    def _handle_tap(self, e):
        e.control.open_view()


"""

def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    patients_list = [f"Patient {i}" for i in range(10)]

    a = Patients(patients_list)
    a.visible = True
    page.add(a)


ft.app(target=main)
"""
