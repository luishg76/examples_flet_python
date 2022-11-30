import flet as ft
from flet import Page, Column, TextField, Text, ElevatedButton 

def main(page:Page):

    first_name=ft.Ref[TextField]()
    last_name=ft.Ref[TextField]() 
    btn_say_hello=ft.Ref[ElevatedButton]()   
    col_tings=Column(controls=[TextField(ref=first_name,label='First Name: ', autofocus=True),
    TextField(ref=last_name,label='Last Name: '),
    ElevatedButton(ref=btn_say_hello,text='Say Hello'),
    ])

    def click_btn(e):
        col_tings.controls.append(Text(value=f'Hello, {first_name.current.value} {last_name.current.value}!',weight="w800"))
        first_name.current.value=''
        last_name.current.value=''        
        page.update()
        first_name.current.focus()
        
    btn_say_hello.current.on_click=click_btn
    page.add(col_tings,ft.Icon(name=ft.icons.ADD_ALARM,color=ft.colors.PINK,size=80))

ft.app(target=main,assets_dir="assets")
