import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT

    hello_text = ft.Text(value="Helooow")

    greeting_history = []  
    history_text = ft.Text("Greeting history:")

    favorites = []         
    favorites_text = ft.Text("Favorites:")
    last_name = {"value": ""} 

    def update_history():
        if greeting_history:
            history_text.value = "Greeting history: ".join(greeting_history)
        else:
            history_text.value = "Greeting history:"

    def update_favorites():
        if favorites:
            favorites_text.value = "Favorites:\n- " + "\n- ".join(favorites)
        else:
            favorites_text.value = "Favorites:"

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

            last_name["value"] = name 

            greeting = f"{timestamp} - {name}"
            greeting_history.append(greeting)

            if len(greeting_history) > 5:
                greeting_history.pop(0)

            update_history()
        else:
            hello_text.value = "Error, enter your name"
            hello_text.color = ft.Colors.RED
        page.update()


    def add_favorite(_):
        name = last_name["value"]
        if name and name not in favorites:
            favorites.append(name)
            update_favorites()
            page.update()

    def clear_history(_):
        greeting_history.clear()
        update_history()
        favorites.clear()
        page.update()

    elevated_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)
    name_input = ft.TextField(label="Enter your name")
    clear_button = ft.IconButton(ft.Icons.CLEAR, tooltip="Clear history", on_click=clear_history)
    favorite_button = ft.ElevatedButton("ADD TO FAVORITES", icon=ft.Icons.STAR, on_click=add_favorite)

    page.add(hello_text,name_input, elevated_button, theme_button, history_text, clear_button, favorite_button, favorites_text)


ft.app(main_page)
