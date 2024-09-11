import flet as ft


class Profile(ft.Card):

    def __init__(self):

        self.profile_pic = ft.Stack(
            [
                ft.CircleAvatar(
                    content=ft.Text(
                        "AA",
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    ),
                    radius=100,
                ),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=10),
                    alignment=ft.alignment.bottom_right,
                ),
            ],
            width=100,
            height=100,
        )

        self.doc_name = ft.Column(
            controls=[
                ft.Text(
                    value="Abdou Sadou",
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    weight="bold",
                ),
                ft.Text(value="Dentist", style=ft.TextThemeStyle.TITLE_MEDIUM),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )

        self.doc_stats = ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            "200",
                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight="bold",
                        ),
                        ft.Text(
                            "Total Patients",
                            style=ft.TextThemeStyle.TITLE_SMALL,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "90",
                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight="bold",
                        ),
                        ft.Text(
                            "Current Patients",
                            style=ft.TextThemeStyle.TITLE_SMALL,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "110",
                            style=ft.TextThemeStyle.TITLE_MEDIUM,
                            weight="bold",
                        ),
                        ft.Text(
                            "Inactive Patients",
                            style=ft.TextThemeStyle.TITLE_SMALL,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        )

        _all_column = ft.Column(
            controls=[self.profile_pic, self.doc_name, self.doc_stats],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        self.all_info = ft.Container(content=_all_column, padding=20)
        super(Profile, self).__init__(content=self.all_info, visible=False)


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    a = Profile()
    page.add(a)


ft.app(target=main, assets_dir="assets")
"""
