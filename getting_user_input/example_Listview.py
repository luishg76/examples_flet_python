import flet as ft
from flet import *

def main(page: ft.Page):
    lv=ListView(expand=True, spacing=10)
    for i in range(5000):        
        lv.controls.append(ft.Text(f"Line {i}"))
    page.add(lv)    

ft.app(target=main, view=ft.WEB_BROWSER)