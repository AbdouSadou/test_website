import flet as ft
from pages import (
    login_page,
    dash_page,
    today_appt,
    patients_page,
    profile_page,
    settings_page,
    support_page,
)


def make_pages(page):
    def _show_dash_page(e):
        for elem in dash_obj.controls:
            elem.visible = False

        dash_obj.controls[e.control.selected_index].visible = True
        e.page.update()

    login_obj = login_page.LoginPage(page)
    login_view = ft.View(
        "/login",
        [login_obj],
        vertical_alignment="center",
        horizontal_alignment="center",
    )

    dash_obj = dash_page.Dashboard(page)
    dash_obj.open_nav_btn.on_click = lambda _: page.open(dash_obj.navbar)
    dash_obj.navbar.on_change = _show_dash_page

    todays_schedule_obj = today_appt.Schedule()
    all_patients = patients_page.Patients(
        patients_list=[f"Patient {i}" for i in range(10)]
    )

    profile_obj = profile_page.Profile()
    settings_obj = settings_page.Settings()
    support_obj = support_page.Support()

    dash_obj.controls.extend(
        [todays_schedule_obj, all_patients, profile_obj, settings_obj, support_obj]
    )

    return login_view, dash_obj
