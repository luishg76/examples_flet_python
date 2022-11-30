import flet as ft
from flet import *

def main(page: ft.Page):
    page.title = "Images Example"    
    page.padding = 50
    page.update()

    img = ft.Image(
        src=f"/icons/icon-512.png",
        width=100,
        height=100,
        fit="contain"
    )

    img2 = ft.Image(
        src=f"/images/pecera.jpg",
        width=200,
        height=200,
        fit="contain"
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(Text('Ejemplo de Carga de un Icono'),img,Text('Ejemplo de Carga de una Imagen Local'),img2,Text('Ejemplo de Carga de Imagenes en Internet'), images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",                               
                width=200,
                height=200,
                fit="fill",
                repeat= "noRepeat",
                border_radius=ft.border_radius.all(10)
            )
        )
    page.update()

ft.app(target=main,assets_dir="assets")
