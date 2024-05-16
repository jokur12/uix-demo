from uix.elements import input, div, form

def input_example():
    with div():
        with form().style("gap: 10px; display: flex; flex-direction: column;"):
            input("", placeholder="Kullanıcı Adı", required=True)
            input("",type="password", placeholder="Şifre", required=True)
            input(type="number", placeholder="Sayı", min=0, max=100)
            input("2024-02-05T00:00",type="datetime-local", placeholder="Tarih ve Saat")
            # datetime-local min ve max attribute değerleri bu type için kullanılamıyor.
            # kontrol için js kullanılabilir veya saat ayrı bir input ile alınabilir. 
            input("",type="date", min="1990-01-01", max="2024-12-31", required=True)
            input("",type="time")
            input("submit", type="submit").cls("btn").style("height: 3rem;")   

title = "Input"
description = '''
## input(value, id, type='text', name, placeholder, required, list, autocomplete, min, max)
1. Temel input elementi.

| attr          | desc                                            |
| :------------ | :-----------------------------------------------|
| id            | Input elementinin id'si                         |
| value         | Input elementinin içeriği                       |
| type          | Input elementinin tipi                          |
| name          | Input elementinin name'i                        |
| placeholder   | Input elementinin placeholder'i                 |
| step          | Input elementinin step'i                        |
| required      | Input elementinin required'u                    |
| list          | Input elementinin list'i                        |
| autocomplete  | Input elementinin autocomplete'i                |
| min           | Input elementinin min değeri (number, range ve date tipi için geçerlidir.) |
| max           | Input elementinin max değeri (number, range ve date tipi için geçerlidir.) |
'''                



    