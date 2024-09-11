import flet as ft


class Support(ft.Column):

    def __init__(self):

        _help_text = ft.Text(
            value="Need Help ?",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            weight=ft.FontWeight.BOLD,
        )
        _help_subtext = ft.Text(
            value="See our FAQ below for how to navigate our app",
            style=ft.TextThemeStyle.TITLE_SMALL,
            weight=ft.FontWeight.NORMAL,
        )

        self.FAQ_card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(
                            name=ft.icons.ARROW_CIRCLE_RIGHT, color=ft.colors.GREEN
                        ),
                        ft.ListTile(
                            title=ft.Text(
                                value="Getting Started",
                                style=ft.TextThemeStyle.BODY_LARGE,
                                weight=ft.FontWeight.BOLD,
                            ),
                            subtitle=ft.Text(
                                value="Everything you need to know to get started and work with our app",
                                style=ft.TextThemeStyle.BODY_MEDIUM,
                                weight=ft.FontWeight.NORMAL,
                            ),
                        ),
                    ]
                ),
                width=400,
                padding=10,
            ),
            elevation=3,
        )

        self.FAQ_grid = ft.GridView(
            expand=True,
            # runs_count=5,
            max_extent=500,
            child_aspect_ratio=2.8,
            spacing=5,
            run_spacing=5,
            controls=[self.FAQ_card for _ in range(5)],
        )
        _contact_text = ft.Text(
            value="Contact Us",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            weight=ft.FontWeight.BOLD,
        )
        _contact_subtext = ft.Text(
            value="Lorem ipsum dolor sit amet dolor sit amet sit amet\ndolor sit amet sit amet...",
            style=ft.TextThemeStyle.TITLE_SMALL,
            weight=ft.FontWeight.NORMAL,
        )

        _image_logo = ft.Image(
            src="favicon.png",
            repeat=ft.ImageRepeat.NO_REPEAT,
            fit=ft.ImageFit.FILL,
            height=100,
            width=100,
        )

        _help_text_column = ft.Column(
            controls=[_help_text, _help_subtext],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        _help_column = ft.Column(
            controls=[_help_text_column, self.FAQ_grid],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        _contact_text_column = ft.Column(
            controls=[_contact_text, _contact_subtext],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        _contact_row = ft.Row(
            controls=[_contact_text_column, _image_logo],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=100,
        )
        super(Support, self).__init__(
            controls=[_contact_row, _help_column],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            expand=True,
            visible=False,
        )


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    a = Support()

    a.visible = True

    page.add(a)


ft.app(target=main, assets_dir="assets")
"""
