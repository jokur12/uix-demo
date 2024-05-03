def f_elements_example():
    return f_elements_example

title="Elements"

description='''

### Elements are the UIX (kind of) equivalent of HTML tags.

### In order to use the elements, you need to include the following line of code in your project.

```python

 from uix.elements import elements, you, want, to, add

```

### To give an example of the use of elements, the following two code blocks provide the same output in general terms.

```python
 
 # UIX button inside div example
 
 with div():
     button("This is a button!")

```

```html

 <!-- HTML button inside div example -->

 <div>
    <button>
        This is a button!
    </button>
 <div>

```

### There are many elements in UIX such as _div, button, textarea, table, td, tr, th, row, col and form_ etc.

### You can use the _with_ keyword to use one element inside another.

```python

 # Example of two labels inside form inside border inside div

 with div():
     with border():
        with form():
            label()
            label()

```
'''
