import flet
from flet import *

def view_setting(page:Page):
    return View(
                    "/settings",
                    [
                       AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                       Text("Settings!", style="bodyMedium"),
                       ElevatedButton("Go to mail settings", on_click=lambda _: page.go("/settings/mail")),
                    ],
                )