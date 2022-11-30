import flet as ft
from flet import *

def main(page:Page):

    def items(count):
        lst_elemts=[]
        for elemnt in range(1, count+1):
            lst_elemts.append(
                Container(
                  content=Text(value=elemnt),
                  width=50,
                  height=50,
                  alignment=Alignment(x=0,y=0),
                  bgcolor=colors.AMBER,
                  border_radius=border_radius.all(5)
                )
            )
        return lst_elemts
    row=Row(controls=items(5), spacing=0)
    
    def slider_change(e):
        row.spacing=int(e.control.value)
        row.update()
    
    myslider=ft.Slider(
        min=0,
        max=50,
        divisions=50,
        value=0,
        label="{value}",
        on_change=slider_change,
    )

    page.add(Column(controls=[Text("Cambie el espacio entre los elementos"),myslider,row]))

app(target=main,view=WEB_BROWSER)            