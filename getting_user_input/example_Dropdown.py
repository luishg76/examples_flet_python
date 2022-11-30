import flet as ft
from flet import *

def main(page:Page):
       lst_colores=["Red", "Blue","Green"]
       txt_select=Text()
       def cargar_colores():
          opciones=[]
          for c in lst_colores:
            opciones.append(dropdown.Option(c))
          return opciones
       def btn_click(e):
          txt_select.value=f"Option Select is: {dwn_colores.value}"
          page.update()
             
       btn_submit=ElevatedButton("Submit",on_click=btn_click)
       dwn_colores=Dropdown(width=100, options=cargar_colores())
       page.add(dwn_colores,btn_submit,txt_select)
ft.app(target=main)