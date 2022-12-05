import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import views.view_root as vr
import views.view_settings as vs
import views.view_setting_emails as vse 

def main(page: Page):
    page.title = "Routes Example"

    print("Initial route:", page.route)

    dic_views={
        "root":vr.view_root(page),
        "settings":vs.view_setting(page),
        "settings-mail":vse.view_setting_emails(page)
    }
    
    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(dic_views["root"])                
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(dic_views["settings"])
        if page.route == "/settings/mail":
            page.views.append(dic_views["settings-mail"])
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

flet.app(target=main, view="web_browser")