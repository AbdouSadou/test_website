import flet as ft
import os

assets_folder_path = os.path.join(os.getcwd(), "assets")

SETTINGS = {
    "use_app_bar": True,
    "default_theme_mode": "dark",
}

ABOUT_APP = {
    "app_icon": os.path.join(assets_folder_path, "app.ico"),
    "app_name": "Modern GUI",
    "app_version": "1.0",
    "about_dialog_title": "About the app",
    "about_dialog_text": "This app was developped using Python and Flet.\nVisit my GitHub repository for some other cool projects",
    "author": "Abdou",
    "show_url_btn_in_dialog": True,
    "url": "https://github.com/abdousadou",
    "url_btn_label": "Visit my Github",
    "url_btn_icon": "INSERT_EMOTICON",
}

NAV_PAGES = {
    "Home": "Home",  # add as many pages as needed
    "Banners": "ANNOUNCEMENT",  # key = title of page, value = icon to use
    "Page 2": ft.icons.PERSON,
    "Cake": "cake",
    "Analytics": "analytics",  # if the icon does not show find something else on here:
}  # https://gallery.flet.dev/icons-browser/

THEME_COLOURS = {
    "pink": ft.colors.PINK_ACCENT_400,
    "purple": ft.colors.PURPLE_ACCENT_400,
    "cyan": ft.colors.CYAN_ACCENT_200,
    "green": ft.colors.GREEN_ACCENT_700,
    "lime": ft.colors.LIME_ACCENT_400,
    "orange": ft.colors.AMBER_ACCENT_400,
    "Default (Blue)": ft.colors.BLUE,
}

BANNER_STATES = {
    "GREEN": [ft.colors.GREEN_500, ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINE)],
    "AMBER": [ft.colors.AMBER_900, ft.Icon(ft.icons.WARNING_AMBER)],
    "RED": [ft.colors.RED_500, ft.Icon(ft.icons.CANCEL_OUTLINED)],
    "DEFAULT": [None],
}

"""
DEFAULT_LIGHT_BGS = [
    light_pic.path
    for light_pic in os.scandir(
        os.path.join(assets_folder_path, "app_backgrounds", "default", "light")
    )
    if light_pic.name.split(".")[-1]
    in ("tif", "tiff", "bmp", "jpg", "jpeg", "gif", "png")
]
CUSTOM_LIGHT_BGS = [
    light_pic.path
    for light_pic in os.scandir(
        os.path.join(assets_folder_path, "app_backgrounds", "custom", "light")
    )
    if light_pic.name.split(".")[-1]
    in ("tif", "tiff", "bmp", "jpg", "jpeg", "gif", "png")
]

DEFAULT_DARK_BGS = [
    dark_pic.path
    for dark_pic in os.scandir(
        os.path.join(assets_folder_path, "app_backgrounds", "default", "dark")
    )
    if dark_pic.name.split(".")[-1]
    in ("tif", "tiff", "bmp", "jpg", "jpeg", "gif", "png")
]
CUSTOM_DARK_BGS = [
    dark_pic.path
    for dark_pic in os.scandir(
        os.path.join(assets_folder_path, "app_backgrounds", "custom", "dark")
    )
    if dark_pic.name.split(".")[-1]
    in ("tif", "tiff", "bmp", "jpg", "jpeg", "gif", "png")
]

WEATHER_ICONS = {
    w_pic.name.split(".")[0]: [w_pic.path]
    for w_pic in os.scandir(
        os.path.join(assets_folder_path, "weather_images", "weather_icons")
    )
}

for w_pic in os.scandir(
    os.path.join(assets_folder_path, "weather_images", "weather_backgrounds", "day")
):
    WEATHER_ICONS[w_pic.name.split(".")[0]].append(w_pic.path)
    WEATHER_ICONS[w_pic.name.split(".")[0]].append(w_pic.path.replace("day", "night"))

weather_widget_height = 200
weather_widget_width = 300

tray_icon = None

 
weather_backgrounds = { "Clouds"       : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Clear"        : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Atmosphere"   : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Snow"         : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Rain"         : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Drizzle"      : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Thunderstorm" : ['icon_path', 'day_bg_path', 'night_bg_path'],
                        "Error"        : ['icon_path', 'day_bg_path', 'night_bg_path']}
"""
