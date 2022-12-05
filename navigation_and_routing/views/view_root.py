import flet
from flet import*

def view_root(page:Page):
   return View(
                "/",
                [
                    AppBar(title=Text("Flet app"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Go to Settings", on_click=lambda _: page.go("/settings")),
                ],
            )