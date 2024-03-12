import os

from aiohttp import web

from nodes import load_custom_nodes
from .lib import backend

def reload_custom_nodes():
    load_custom_nodes()
    return web.Response(text="loaded custom nodes")


# Initial load of the devkit
if "DEVKIT_LOADED" not in os.environ:
    server = backend.Backend('devkit')
    server.add_route("GET", "reload", lambda x: reload_custom_nodes())
    os.environ["DEVKIT_LOADED"] = "True"



print("ComfyDevKit loaded")

def transform_css_to_js(css_content):
    js_content = """
    var docStyle = document.createElement('style');
docStyle.innerHTML = `""" + css_content.replace('`', r'\`').replace('\\', r'\\') + """
`;
document.head.appendChild(docStyle);
    """
    return js_content


# comfy doesn't load css files, so we need to convert them to js
def transform_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".css"):
            css_file_path = os.path.join(folder_path, filename)
            js_file_path = os.path.join(folder_path, filename[:-4] + ".css.js")

            with open(css_file_path, 'r') as css_file:
                css_content = css_file.read()

            js_content = transform_css_to_js(css_content)

            with open(js_file_path, 'w') as js_file:
                js_file.write(js_content)


WEB_DIRECTORY = 'dist'

script_directory = os.path.dirname(os.path.realpath(__file__))
javascript_folder = os.path.join(script_directory, WEB_DIRECTORY)
transform_files_in_folder(javascript_folder)

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
