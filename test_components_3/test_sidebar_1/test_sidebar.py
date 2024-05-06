import uix
from uix.elements import div, link,input,label,span,col,icon, unorderedlist, listitem
from uix.core.session import context
import os
import importlib



uix.html.add_css_file("test_sidebar.css",__file__)
uix.html.add_script_source(id="test_sidebar",script="test_sidebar.js",beforeMain=False,localpath=__file__)
path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_sidebar")
uix.app.add_static_route("test_sidebar",path)

def get_current_list():
    for list_item in lists:
        if context.session.paths[0] == list_item["title"]:
            return list_item
    return None

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

filter_str = ""

class test_sidebar(uix.Element):
    def __init__(self, value=None, id=None):
        super().__init__(value, id)
        def filter_menu(ctx, id, value):
                global filter_str
                filter_str = value
                print(value)
                ctx.elements["ftr_result"].update(filtrele)
        with self.style("width:0px;"):
            with div().cls("test-sidebar-1") as menu:
                
                    input(value="",id="menu_active",type="checkbox")
                    

                    with div(id="wrapper").cls("active"):
                        with div(id="menu"):
                            # link(id="nav-title",value="&nbsp;",href="")
                            with span(id="site_name"):
                                with label(usefor="menu_active"):
                                    with div(id="icons"):    
                                        icon(value="fa fa-arrow-left")
                                        icon(value="fa fa-bars")
                                    with div(id="ftr"):
                                        input(id="ftr", placeholder="Filtrele").cls("ftr-input").on("input",filter_menu)
                            def filtrele():
                                with unorderedlist().cls("ul")as liste:
                                    with listitem().cls("li"):
                                        current_list = get_current_list()
                                        if current_list:
                                            for item in current_list["list"]:
                                                if filter_str.lower() in item.lower():
                                                    item_without_spaces=item.replace("_"," ")
                                                    if len(context.session.paths) > 1 and context.session.paths[1] == item:
                                                        link(item_without_spaces.title(), href=f"/{current_list['title']}/{item}").cls("button")
                                                    else:
                                                        link(item_without_spaces.title(), href=f"/{current_list['title']}/{item}").cls("button-inactive")
                                    return liste
                            with div(id="ftr_result").cls("ftr-result"):
                                filtrele()            
                   
                        
                    # with input("", placeholder="Filtrele" ,id="filtre").style("margin-bottom: 5px;justify-content:center;").cls("filter-input").on("input", filter_menu):
                    #     pass
                    # with div(id="nav-content").cls("nav-content"):
                    #     #input("", placeholder="Filtrele" ,id="filtre").style("margin-bottom: 10px;justify-content:center;").cls("filter-input").on("input", filter_menu)
                        

                    

                    
              