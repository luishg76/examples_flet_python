import flet
from flet import Page, Row, Text

def main(page:Page):
    lenguajes=['Python','Flet','Flutter']
    controles=[]
    for l in lenguajes:
        controles.append(Text(l))
    page.add(Row(controls=controles))

flet.app(target=main)
