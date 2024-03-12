# Backend

Sometimes you may want to send a request from the frontend to python, in order to do that you can use the `backend`.
first, import it:
```python
from .lib import backend
```

Then you can use it like this:
```python
from aiohttp import web
from .lib import backend

server = backend.Backend('your-app-name')
async def hello(request):
    return web.Response(text="Hello, world!")

server.add_route('GET', 'hello', hello)
```

Notice that backend uses aiohttp, so you can use the `web` module to create a response.


After that, you call the route you just created from the frontend using regular fetch:
```javascript
fetch('/<your-app-name>/hello').then(response => response.text()).then(console.log)
```


Considering the fact that you are developing a plugin and name conflicts might happen, the backend is namespaced with the app name, so you can use the same route name in different plugins without conflicts.
If you want finer control, you can see how the backend is implemented in the `lib/backend.py`.


If you intend on using the reload functionality, you should avoid calling add_route multiple times. you can call it once like this:
```python
if "APP_NAME_LOADED" not in os.environ:
    server = backend.Backend('APP_NAME')
    server.add_route("GET", "action", ...)
```