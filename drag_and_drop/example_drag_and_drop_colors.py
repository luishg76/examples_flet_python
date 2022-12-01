import flet as ft
from flet import *

def main(page:Page):
    page.title="Drag and drop colors example"   

    def drag_will_accept(e):
        e.control.content.border=border.all(2,colors.RED
        if e.data=="true" else colors.BLACK45)
        e.control.update()

    def drag_accept(e):
        source=page.get_control(e.src_id)
        e.control.content.bgcolor=source.content.bgcolor
        e.control.content.border=border.all(1,colors.BLACK45)
        e.control.update()

    def drag_leave(e):
        e.control.content.border=border.all(1,colors.BLACK45)
        e.control.update()

    def container_color(bgcolor:colors,bcolor=colors.BLACK45):
        return Container(
                            bgcolor=bgcolor,
                            border=border.all(1,bcolor),
                            width=50,
                            height=50,
                            border_radius=border_radius.all(5)
                        )
    def container_feedback_color(bgcolor:colors,bcolor=colors.BLACK45):
        return Container(
                            bgcolor=bgcolor,
                            border=border.all(1,bcolor),
                            width=20,
                            height=20,
                            border_radius=border_radius.all(3)
                        )
    page.add(Row(
         [Column(
            [
                Draggable(
                    group="colors",
                    content=container_color(colors.BLUE),
                    content_feedback=container_feedback_color(colors.BLUE)
                    ),
                Draggable(
                    group="colors",
                    content=container_color(colors.YELLOW),
                    content_feedback=container_feedback_color(colors.YELLOW)
                    ),
                Draggable(
                    group="colors",
                    content=container_color(colors.GREEN),
                    content_feedback=container_feedback_color(colors.GREEN)
                    )
            ]
         ),
         Column([Container(width=100)]),
         Column([
                  DragTarget(
                    group="colors",
                    content=container_color(colors.WHITE10),
                    on_will_accept=drag_will_accept,
                    on_leave=drag_leave,
                    on_accept=drag_accept
                    )
                ]
         )]
    ))
    
app(target=main)  
