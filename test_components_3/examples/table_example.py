import uix
from uix.elements import table, tr, td, tbody, th, thead, row # type: ignore
from uix.elements._table import title, description, sample as code

uix.html.add_css("custom-table","""
:root {
/* 0px yazılırsa ilgili çizgi kaldırılmış olur */                  
    --dikeycizgiler: 1px solid black;
    --yataycizgiler: 3px solid gray;
}

/* BORDER none yapılarak sıfırlanıyor */                           
#custom-table, #custom-table th, #custom-table td {
    border: none;
    border-collapse: collapse;
}
#custom-table th, #custom-table td {
    border-right: var(--dikeycizgiler);
    border-left: var(--dikeycizgiler);
}
                
#custom-table tr, #custom-table td {
    border-bottom: var(--yataycizgiler);
    border-top: var(--yataycizgiler);
}                                                  
                                
#custom-table thead {    
  background-color: #ff000026;
} 

#custom-table tr:nth-child(even){ 
  background-color: initial;    //Zebra efekti kaldırılmış olur. İstenirse başka renkte verilebilir.
}
""")


fake_data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "leannge@gmail.com"
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "ervin@gmail.com"
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "clementine@gmail.com"
    },
    {
        "id": 4,
        "name": "Patricia Lebsack",
        "username": "Karianne",
        "email": "patricia@gmail.com"
    },
    {
        "id": 5,
        "name": "Chelsey Dietrich",
        "username": "Kamren",
        "email": "chelsey@gmail.com"
    }
]

def table_example():
    global fake_data
    with row().style("width: max-content; gap: 10px;"):
        with table("", id="table_example"):
            with thead("",id="table_example_header"):
                with tr("",id="table_example_header_row"):
                    th("ID")
                    th("Name")
                    th("Username")
                    th("Email")
            with tbody("",id="table_example_body"):
                for item in fake_data:
                    with tr("",id=item["id"]):
                        td(item["id"])
                        td(item["name"])
                        td(item["username"])
                        td(item["email"])

        with table("", id="custom-table"):
            with thead(""):
                with tr(""):
                    th("ID")
                    th("Name")
                    th("Username")
                    th("Email")
            with tbody("",id="custom-table_body"):
                for item in fake_data:
                    with tr("",id="custom-"+str(item["id"])):
                        td(item["id"])
                        td(item["name"])
                        td(item["username"])
                        td(item["email"])
                    