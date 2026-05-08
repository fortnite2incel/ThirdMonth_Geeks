import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    hello_text = ft.Text(value="Helooow")
    # # Option A: Seed a color palette (easiest)
    # page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    
    def theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.text = "LIGHT MODE"
            theme_button.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.text = "DARK MODE"
            theme_button.icon = ft.Icons.DARK_MODE
        page.update()


    
    theme_button = ft.ElevatedButton(
        "DARK MODE",
        icon=ft.Icons.DARK_MODE,
        on_click=theme
    )

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            timestamp = now.strftime("%Y:%m:%d - %H:%M:%S")
            hello_text.color = None
            hello_text.value = f"{timestamp} - Привет, {name}!"
        else:
            hello_text.value = "Error, enter your name"
            hello_text.color = ft.Colors.RED
        page.update()

    elevated_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)

    name_input = ft.TextField(label="Enter your name")

    
        # ft.run(main_page, view =fit.AppView.WEB_BROWSER)
    page.add(hello_text, name_input, elevated_button, theme_button)

ft.run(main_page)

