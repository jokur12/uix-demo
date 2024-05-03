def k_using_javascript_example():
    return k_using_javascript_example

title="Using JavaScript"

description='''

### There are 2 ways to use JavaScript in UIX

### These ways of use are as follows:

### 1) Internal JavaScript
### 2) External JavaScript

## Internal JavaScript

---

### To use Internal JavaScript, you need to use the _add_script_ method.
### An example of the use of this method is given below

```python

 # UIX internal JavaScript example


 uix.html.add_script("script.js",
 """

 alert("This is an alert!")

 
 """, beforeMain=False)

```
## External JavaScript

---

### To use external JavaScript, you need to add the JavaScript file using the _add_script_source_ method.
### An example of the use of this method is given below

```python

 # UIX external JavaScript example

 uix.html.add_script_source(id="script",script="script.js",beforeMain=False,localpath=__file__)

```

```javascript

 // script.js

 alert("This is an alert!")

```

### Note: beforeMain is used to determine whether the script will run before or after the main function.
'''
