from uix.elements import md2

def md_example():
    main = md2('''# Hello World!
```python
from uix.elements import div

def hello_world_example():
    main = div("Hello World!").style("font-size","30px")
    return main
```
               ''')
    return main