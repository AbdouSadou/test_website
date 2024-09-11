import flet as ft
import datetime


class Schedule(ft.Column):
    def __init__(self):

        self.calendar = ft.DatePicker(
            open=False,
            first_date=datetime.datetime(year=2023, month=1, day=1),
            last_date=datetime.datetime(year=2025, month=12, day=31),
            field_hint_text=datetime.datetime.today(),
            on_dismiss=self._handle_dismissal,
            on_change=self._handle_dismissal,
        )

        super(Schedule, self).__init__(
            controls=[
                self.calendar,
                ft.ElevatedButton(
                    "Pick date",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: e.page.open(self.calendar),
                ),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            visible=True,
        )

    def _handle_dismissal(self, e):
        e.control.open = False
        e.page.update()


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    a = Schedule()
    page.add(a)


ft.app(target=main)
"""
