from flet import *

def main(page: Page):
    t=Text(value="Hello, World!", color="green")
    page.controls.append(t)    
    page.update()
    sleep(1)
    for i in range(10):
        t.value=f"Step {i}"
        page.update()
        sleep(1)


app(target=main,view=FLET_APP)