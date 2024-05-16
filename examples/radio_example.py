from uix.elements._radio import radio
from uix.elements._div import div


def radio_example():
    with div().cls('row').style("width","fit-content").style("margin-bottom","20px"):
        radio("Radio 1","Radio 1",name="radio1").on("change", on_change)
        radio("Radio 2","Radio 2",name="radio1").on("change", on_change)
        radio("Radio 3","Radio 3", name="radio1").on("change", on_change)
        div("Test","Test")

def on_change(ctx, id, value):
    print("Changed", id, value)
    if id == "Radio 4":
        ctx.elements["Test"].value = "Peki"
        ctx.elements["Test"].update()
    else:
        ctx.elements["Test"].value = id
        ctx.elements["Test"].update()

title = "Radio"
description = """
## radio(value,id,name)
1. Temel HTML radio elementi.

| attr          | desc                                            |
| :------------ | :-----------------------------------------------|
| id            | radio elementinin id'si                         |
| value         | radio elementinin değeri                        |
| name          | radio elementinin bağlı olduğu grubun adı       |
"""