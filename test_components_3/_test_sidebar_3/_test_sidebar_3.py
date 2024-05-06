import uix
from uix.elements import div, link,input,label,span,col
from uix.core.session import context
import os
import importlib


uix.html.add_css_file("_test_sidebar_3.css", __file__)
uix.html.add_script_source(id="_test_sidebar_3",script="_test_sidebar_3.js",beforeMain=False,localpath=__file__)
path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "_test_sidebar_3")
uix.app.add_static_route("_test_sidebar_3",path)

#def filter_menu(ctx, id, value):
#    global filter_str
#    filter_str = value
#    print(value)
#    ctx.elements["filtre_result"].update(test_sidebar_3)


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

class test_sidebar_3(uix.Element):
    def __init__(self, value=None, id=None):
        super().__init__(value, id)
        def filter_menu(ctx, id, value):
                global filter_str
                filter_str = value
                print(value)
                ctx.elements["filtre_result"].update(filtreleme)
        
                
        with self:
            with div().cls("test-sidebar-3") as menu:
                pass

                with div(id="nav-bar").style("border-radius:5px").cls("nav-bar"):
                    input(value="",id="nav-toggle",type="checkbox",name="nav-toggle")

                    with div(id="nav-header").cls("nav-header"):
                        link(id="nav-title",value="&nbsp;",href="")
                        with label(usefor="nav-toggle"):
                            span(id="nav-toggle-burger")
                        
                    with input("", placeholder="Filtrele" ,id="filtre").style("margin-bottom: 5px;justify-content:center;").cls("filter-input").on("input", filter_menu):
                        pass
                    with div(id="nav-content").cls("nav-content"):
                        #input("", placeholder="Filtrele" ,id="filtre").style("margin-bottom: 10px;justify-content:center;").cls("filter-input").on("input", filter_menu)
                        

                        def filtreleme():
                            with col(id="nav-button").cls("nav-button")as liste:
                            
                                current_list = get_current_list()
                                if current_list:
                                    for item in current_list["list"]:
                                        if filter_str.lower() in item.lower():
                                            item_without_spaces=item.replace("_"," ")
                                            if len(context.session.paths) > 1 and context.session.paths[1] == item:
                                                link(item_without_spaces.title(), href=f"/{current_list['title']}/{item}").cls("nav-button").style("text-decoration: none; margin-bottom: 10px; border: 0.1px solid var(--ait);background-color:var(--ait); width: 220px; justify-content: left;align-items: center;border-radius: 5px;margin-top: 10px;").style("color", "white")
                                            else:
                                                link(item_without_spaces.title(), href=f"/{current_list['title']}/{item}").cls("nav-button-inactive").style("text-decoration: none; margin-bottom: 10px;  width: 220px; justify-content: left;align-items: center;border-radius: 5px ;margin-top: 10px;").style("color", "white")    
                                return liste          
                        with div(id="filtre_result").cls("filter-result"):
                            filtreleme()

                        with div(id="nav-content-highlight").cls("nav-content-highlight"):
                            pass
                
              