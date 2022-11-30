import flet as ft
from flet import Page, Row, Column, ElevatedButton, Checkbox, TextField

def main(page:Page):
      lst_tareas=Column()
      txttarea=TextField(label="Whats needs to be done?:")
      def Agregar_Tarea(e):
          lst_tareas.controls.append(Checkbox(label=txttarea.value))
          txttarea.value=""
          page.update()

      page.add(Column(controls=[Row(controls=[txttarea, ElevatedButton("Add", on_click=Agregar_Tarea)]), lst_tareas]))
ft.app(target=main)