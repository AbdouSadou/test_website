import flet as ft
import time


class LoginPage(ft.Container):

    def __init__(self, page):

        self.page = page

        self.dark_theme_switcher = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.DARK_MODE,
                    icon_size=20,
                    tooltip="Switch to dark mode",
                    on_click=self._switch_dark_theme,
                )
            ],
            alignment=ft.MainAxisAlignment.END,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        bubble1 = ft.Container(
            animate=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
            width=10,
            height=20,
            border_radius=100,
            bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
        )
        bubble2 = ft.Container(
            animate=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
            width=10,
            height=20,
            border_radius=100,
            bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
        )
        bubble3 = ft.Container(
            animate=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
            width=10,
            height=20,
            border_radius=100,
            bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
        )
        bubble4 = ft.Container(
            animate=ft.animation.Animation(400, ft.AnimationCurve.DECELERATE),
            width=10,
            height=20,
            border_radius=100,
            bgcolor=ft.colors.ON_PRIMARY_CONTAINER,
        )
        self.loading_animation = ft.Row(
            alignment="center",
            controls=[bubble1, bubble2, bubble3, bubble4],
            visible=False,
        )
        self.app_icon = ft.Container(
            image_src="favicon.png",
            image_fit=ft.ImageFit.FILL,
            image_repeat=ft.ImageRepeat.NO_REPEAT,
            rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
            animate_rotation=ft.animation.Animation(
                1000, ft.AnimationCurve.EASE_OUT_CUBIC
            ),
            width=100,
            height=100,
        )

        self.username_field = ft.TextField(
            label="Username",
            prefix_icon=ft.icons.PERSON_OUTLINED,
            hint_text="Please enter your username",
        )
        self.password_field = ft.TextField(
            label="Password",
            prefix_icon=ft.icons.LOCK_OUTLINED,
            password=True,
            can_reveal_password=True,
            hint_text="Please enter your password",
        )

        self.login_button = ft.FilledButton(
            content=ft.Column(
                controls=[self.loading_animation, ft.Text(value="Login")],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=370,
            height=45,
            disabled=False,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=10,
                bgcolor={
                    ft.ControlState.PRESSED: ft.colors.GREEN_100,
                    ft.ControlState.DEFAULT: ft.colors.PRIMARY,
                    ft.ControlState.DISABLED: ft.colors.PRIMARY_CONTAINER,
                },
            ),
            on_click=self._handle_login,
        )
        self.remember_login = ft.Checkbox(
            adaptive=True, label="Remember me?", value=True
        )

        self.login_display_text = ft.Container(
            ft.Text(
                "Log in to continue",
                style=ft.TextThemeStyle.TITLE_MEDIUM,
                visible=True,
                weight="bold",
            )
        )
        self.content_column = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            height=560,
            width=360,
        )

        self.content_column.controls.extend(
            [
                self.dark_theme_switcher,
                self.app_icon,
                self.login_display_text,
                self.username_field,
                self.password_field,
                self.login_button,
                self.remember_login,
            ]
        )

        # self._animate_logo

        super(LoginPage, self).__init__(
            content=self.content_column,
            padding=10,
            border=ft.border.all(2, ft.colors.PRIMARY),
            border_radius=ft.border_radius.all(20),
            height=600,
            width=400,
        )

    def _switch_dark_theme(self, e):
        if self.page.theme_mode == "light":
            self.page.theme_mode = "dark"
            self.dark_theme_switcher.controls[0].icon = ft.icons.LIGHT_MODE
            self.dark_theme_switcher.controls[0].tooltip = "Switch to light mode"
        else:
            self.page.theme_mode = "light"
            self.dark_theme_switcher.controls[0].icon = ft.icons.DARK_MODE
            self.dark_theme_switcher.controls[0].tooltip = "Switch to dark mode"
        self.page.update()

    def _login_animation(self):
        self.login_button.disabled = True
        self.page.update()
        start = -1
        i = 3
        while i >= 0:
            if start == -1:
                self.loading_animation.controls[0].height = 30
                self.page.update()
                start = 1
            else:
                time.sleep(0.3)
                self.loading_animation.controls[-1].height = 20
                self.loading_animation.controls[0].height = 30
                self.page.update()
            time.sleep(0.3)
            self.loading_animation.controls[0].height = 20
            self.loading_animation.controls[1].height = 30
            self.page.update()
            time.sleep(0.3)
            self.loading_animation.controls[1].height = 20
            self.loading_animation.controls[-2].height = 30
            self.page.update()
            time.sleep(0.3)
            self.loading_animation.controls[-2].height = 20
            self.loading_animation.controls[-1].height = 30
            self.page.update()
            i -= 1
        self.page.update()

    def _handle_login(self, e):

        # TODO: Design consistent usernames, then use regex here
        forbidden = ("", " ")
        if (
            self.password_field.value in forbidden
            or self.username_field.value in forbidden
        ):
            self.password_field.error_text = "Please enter a valid password!"
            self.username_field.error_text = "Please enter a valid username!"
            self.login_button.style.bgcolor = {
                ft.ControlState.DEFAULT: ft.colors.PRIMARY
            }

        else:
            self.password_field.error_text = ""
            self.username_field.error_text = ""
            self.login_button.content.controls[1].visible = False
            self.login_button.content.controls[0].visible = True

            self._login_animation()
            self.page.go("/dash")

        self.page.update()

        # TODO: REMEMBER ME CHECKBOX  https://flet.dev/docs/cookbook/authentication / https://flet.dev/docs/cookbook/session-storage

        print(f"EYYYYYYY WELCOME DOC! {e}")

        print(self.page.route)

        self.page.update()


"""
def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "TESTING"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    a = LoginPage(page)
    page.add(a)


ft.app(target=main)
"""
