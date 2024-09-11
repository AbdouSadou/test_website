import flet as ft
from statics import THEME_COLOURS


class Settings(ft.Card):
    def __init__(self):
        self.dark_theme_switcher = ft.Switch(
            label="Switch to dark mode",
            on_change=self._switch_dark_theme,
            value=False,
        )

        self.themes_dropdown = ft.Dropdown(
            hint_text="Choose a theme colour",
            on_change=self._set_theme_color,
            prefix_icon="color_lens",
            options=[
                ft.dropdown.Option(text=f"{_color_.title()}")
                for _color_ in THEME_COLOURS
            ],
        )

        _theming_panel = ft.ExpansionPanel(
            header=ft.ListTile(
                title=ft.Text(f"Theming options"),
                leading=ft.Icon(name="brush"),
            ),
            expanded=False,
            can_tap_header=True,
            content=ft.Column(
                controls=[self.dark_theme_switcher, self.themes_dropdown]
            ),
        )
        _misc_panel = ft.ExpansionPanel(
            header=ft.ListTile(
                title=ft.Text(f"Other options"),
                leading=ft.Icon(name="settings"),
            ),
            expanded=False,
            can_tap_header=True,
        )

        self.options_panel_list = ft.ExpansionPanelList(
            # expand_icon_color=ft.colors.AMBER,
            # elevation=8,
            # divider_color=ft.colors.AMBER,
            spacing=30,
            controls=[_theming_panel, _misc_panel, _misc_panel],
        )

        self.persistent_check = ft.Container(
            ft.Checkbox(
                label="Make changes persistent for this user?",
                value=True,
                adaptive=True,
            ),
            alignment=ft.alignment.center,
            padding=20,
        )

        self.all_settings = ft.Column(
            controls=[
                self.options_panel_list,
                self.persistent_check,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

        super(Settings, self).__init__(content=self.all_settings, visible=False)

    def _set_theme_color(self, e):

        e.page.dark_theme = e.page.theme = ft.Theme(
            color_scheme_seed=e.control.value.split(" ")[-1]
            .replace("(", "")
            .replace(")", "")
            .lower(),
            visual_density=ft.ThemeVisualDensity.COMPACT,
        )
        e.control.label = (
            "Good choice!" if e.control.label != "Good choice!" else "Beautiful!"
        )
        e.page.update()

    def _switch_dark_theme(self, e):
        if e.page.theme_mode == "light":
            e.page.theme_mode = "dark"
            self.dark_theme_switcher.value = True
            self.dark_theme_switcher.label = "Switch to light mode"
        else:
            e.page.theme_mode = "light"
            self.dark_theme_switcher.value = False
            self.dark_theme_switcher.label = "Switch to dark mode"
        e.page.update()


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # patients_list = [f"Patient {i}" for i in range(10)]

    a = Settings()
    a.visible = True
    page.add(a)


ft.app(target=main)
"""
