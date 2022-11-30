import os
import flet
from flet import *

os.environ["FLET_WS_MAX_MESSAGE_SIZE"]='8000000'

def main(page:Page):
    gv=GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
      gv.controls.append(
        Container(
            Text(f"Items: {i}"),
            alignment=alignment.center,
            width=100,
            height=100,
            bgcolor=colors.AMBER_100,
            border=border.all(1,colors.AMBER_400),
            border_radius=border_radius.all(5)
        )
      )
    page.update()

app(target=main,view=WEB_BROWSER)