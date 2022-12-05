import flet
from flet import*

def view_setting_emails(page:Page):
    return View(
                    "/settings/mail",
                    [
                        AppBar(
                            title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Mail settings!"),
                        ElevatedButton("Home", on_click=lambda _:page.go("/"))
                    ],
                ) 