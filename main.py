import flet as ft

def main_page(page: ft.Page):
    hello_text = ft.Text(value= "Helooow")
    page.add(hello_text)

    

ft.run(main_page)