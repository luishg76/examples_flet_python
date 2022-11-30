from flet import*

def main(page:Page):
    txtnombre=TextField(label="Entre su Nombre:")    
    txtsaludo=Text()
    def saludar(e):
        txtsaludo.value=f"¡Hola {txtnombre.value}"
        page.update()

    page.add(Row(controls=[txtnombre, ElevatedButton("Saludar", on_click=saludar), txtsaludo]))

app(target=main)