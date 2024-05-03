def i_using_css_example():
    return i_using_css_example

title="Using CSS"

description='''

### In UIX, you can use CSS in three different ways, just like HTML.

### These ways of use are as follows:

### 1) Inline CSS
### 2) Internal CSS
### 3) External CSS

## Inline CSS

---

### To use inline CSS, you need to add the _.style()_ method to the element you want to style.

```python

 # UIX inline CSS example

 button("Click Me!").style("padding: 20px; margin-left: 10px;")

```
## Internal CSS

---

### To use Internal CSS, you need to write your css codes with the _add_css_ method.
### An example of the use of this method is given below

```python

 # UIX internal CSS example

 uix.html.add_css("style.css",

 """
 button {
    
    padding: 20px;
    margin-left: 10px;

 }
 """
 )

```
## External CSS

---

### To use external CSS, you need to add the CSS file using the _add_css_file_ method.
### An example of the use of this method is given below

```python

 # UIX external CSS example

 uix.html.add_css_file("style.css", __file__)

```

```css

 /* style.css */

 button {
 
  padding: 20px;
  margin-left: 10px;

 }

```
'''
