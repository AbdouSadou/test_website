import flet as ft
from pages import pages_manager


def main(page):
    page.adaptive = True

    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    theme = ft.Theme()
    theme.page_transitions.linux = ft.PageTransitionTheme.FADE_UPWARDS
    page.theme = theme
    page.update()

    login_view, dash_view = pages_manager.make_pages(page)

    def route_change(e):
        e.page.views.clear()
        e.page.views.append(login_view)
        if e.page.route == "/dash":
            e.page.views.append(dash_view)
        e.page.update()

    def view_pop(e):
        e.page.views.pop()
        top_view = e.page.views[-1]
        e.page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")


ft.app(main, assets_dir="assets")
