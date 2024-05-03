def e_getting_started_example():
    return e_getting_started_example

title="Getting Started"

description='''

### To get started with UIX, you can paste the following code into a new Python file and run it.

```python

 import uix
 from uix.elements import md
 from uix.pipes import status_pipe

 def root():
     md("# Hello UIX!")

 uix.start(ui = root,config = {"debug" : True, "pipes":[status_pipe()], "locales_path":"locale"})

```

### After navigating to _localhost:5000_ in your browser this executed code should print 
# Hello UIX!
### on your screen. 
'''
