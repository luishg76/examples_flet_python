import flet
from flet import *

def main(page:Page):
    page.title="Drag and Drop example"

    def on_accept(e):
        source=page.get_control(e.src_id)
        source.content.content.value='0'
        source.content.bgcolor=colors.PINK_200
        e.control.content.content.value='1'
        e.control.content.bgcolor=colors.CYAN_200
        page.update()

    page.add(Row([Draggable(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.CYAN_200,
                        border_radius=border_radius.all(5),
                        content=Text("1", size=20),
                        alignment=alignment.center,
                    )
                ),
                Container(width=100),
                DragTarget(
                    group="number",
                    content=Container(
                        width=50,
                        height=50,
                        bgcolor=colors.PINK_200,
                        border_radius=border_radius.all(5),
                        content=Text("0", size=20),
                        alignment=alignment.center,
                    ),
                    on_accept=on_accept
                )])
    )  

app(target=main)
