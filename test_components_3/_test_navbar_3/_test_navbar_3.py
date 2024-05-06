import uix
from uix.elements import link, row, div
from uix.core.session import context
import os
import importlib

uix.html.add_css_file("_test_navbar_3.css", __file__)

def get_info_from_folder(folder_path, folder_name):
    all_items = {}
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".py"):
            module_name = f"{folder_name}.{file_name[:-3]}"
            module = importlib.import_module(module_name)
            all_items[file_name[:-11]] = {
                "module": module,
                "name": module.__name__,
                "title": getattr(module, "title", file_name[:-11]),
                "description": getattr(module, "description", ""),
                "code": getattr(module, "code", "")
            }
    return all_items

examples = get_info_from_folder("examples", "examples")
components = get_info_from_folder("examples/components", "examples.components")
test_introductions_3 = get_info_from_folder("test_components_3/test_introductions_3", "test_components_3.test_introductions_3")

lists = [
    {
        "title": "introductions",
        "list": test_introductions_3
    },
    {
        "title": "examples",
        "list": examples
    },
    {
        "title": "components",
        "list": components
    }
]

class test_navbar_3(uix.Element):
    def __init__(self, value=None, id=None):
        super().__init__(value, id)
        with self:
            with div("").cls("test-navbar-3-row"):
                for list_item in lists:
                    if context.session.paths[0] == list_item["title"]:
                            link(list_item["title"], href=f"/{list_item['title']}").cls("btn test-navbar-3-button test-navbar-3-button-active").style("text-decoration", "none").style("color", "white")
                    else:
                            link(list_item["title"], href=f"/{list_item['title']}").cls("btn btn-inactive test-navbar-3-button test-navbar-3-button-inactive").style("text-decoration", "none").style("color", "white")
