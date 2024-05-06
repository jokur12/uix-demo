from uix.elements import col
from uix_components import basic_prompt

def prompt_example():
    with col() as content:
        basic_prompt("", id = "myPrompt")
    return content

title="Prompt Example"

description = '''
    Prompt example shows how to create a prompt component.
'''

code = """
import uix
import uix_components
from uix.elements import col
from uix_components import basic_prompt

def prompt_example():
    with col() as content:
        basic_prompt("", id = "myPrompt")
    return content
"""