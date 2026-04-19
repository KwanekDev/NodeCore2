# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0


from Classes._runtime import Runtime
from Core.Requests import Requests
from Core.Dispatcher import Dispatcher

services = {
    "test": ["python", "-m", "http.server", "8000"]
}

runtime = Runtime(services)
dispatcher = Dispatcher(runtime)
handler = Requests(dispatcher)

while True:
    raw = input(">>> ")
    request = {"command": raw.strip(), "args": {}}
    response = handler.handle(request)
    print(response)