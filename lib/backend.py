import server
import gc
promptServer = None
for obj in gc.get_objects():
    if isinstance(obj, server.PromptServer):
        promptServer = obj
        break
class Backend:
    def __init__(self, appName):
        self.appName = appName
        # Steal server object from ComfyUI. Muahaha!
        self.promptServer = promptServer

    def add_route(self, method, path, handler):
        print(f"Adding route /{self.appName}/{path}")
        # add /appName/path to the server
        self.promptServer.app.router.add_route(method, f'/{self.appName}/{path}', handler)
