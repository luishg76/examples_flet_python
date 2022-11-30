from flet import *

def main(page: Page):
    page.title='Flet counter example'
    page.vertical_alignment="center"

    txt_number=TextField(value="0", text_align="right",width=100)
    
    def decrement(event):
        print('decrement')
        txt_number.value=int(txt_number.value)-1
        page.update()

    def increment(event):
        print('inecrement')
        txt_number.value=int(txt_number.value)+1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE_CIRCLE, on_click=decrement),
                txt_number,
                IconButton(icons.ADD_CIRCLE, on_click=increment)
            ],
            alignment="center"
            )
        )

#modo Desktop:        
#app(target=main)

#modo Web
app(target=main,view=WEB_BROWSER)

