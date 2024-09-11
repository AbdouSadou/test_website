import flet as ft


class Dashboard(ft.View):
    def __init__(self, page):

        self.navbar = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    label="Upcoming Appointements",
                    icon=ft.icons.CALENDAR_MONTH_OUTLINED,
                    selected_icon=ft.icons.CALENDAR_MONTH,
                ),
                ft.Divider(thickness=1),
                ft.NavigationDrawerDestination(
                    label="All Patients",
                    icon=ft.icons.PERSON_PIN_OUTLINED,
                    selected_icon=ft.icons.PERSON_PIN_ROUNDED,
                ),
                ft.NavigationDrawerDestination(
                    label="Doctor Profile",
                    icon=ft.icons.ACCOUNT_CIRCLE_OUTLINED,
                    selected_icon=ft.icons.ACCOUNT_CIRCLE,
                ),
                ft.NavigationDrawerDestination(
                    label="App Settings",
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                ),
                ft.Divider(thickness=1),
                ft.NavigationDrawerDestination(
                    label="App Support",
                    icon=ft.icons.HELP_OUTLINE,
                    selected_icon=ft.icons.HELP,
                ),
            ],
            tile_padding=10,
            indicator_shape=ft.RoundedRectangleBorder(radius=5),
            open=True,
        )

        self.open_nav_btn = ft.FloatingActionButton(
            icon=ft.icons.DASHBOARD,
            mini=True,
        )

        super(Dashboard, self).__init__(
            "/dash",
            vertical_alignment="center",
            horizontal_alignment="center",
            floating_action_button=self.open_nav_btn,
            floating_action_button_location=ft.FloatingActionButtonLocation.START_TOP,
            drawer=self.navbar,
        )


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    a = Dashboard(page)

    page.views.append(a)
    page.go("/dash")


#    page.add(a)


ft.app(target=main)
"""
