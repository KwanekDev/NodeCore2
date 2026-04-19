# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

from pathlib import Path
from Classes._runtime import Runtime
from Core.Requests import Requests
from Core.Dispatcher import Dispatcher


#This is for prototyping only
MODULES_DIR = Path("Examples")

def setup_services(dir):
    result = {}

    if dir.exists() and dir.is_dir():
        for script in dir.glob("*.py"):
            if not script.name.startswith("_"):
                result[script.stem] = ["python", str(script)]

    return result

services = setup_services(MODULES_DIR)

runtime = Runtime(services)
dispatcher = Dispatcher(runtime)
handler = Requests(dispatcher)

while True:
    raw = input(">>> ")
    request = {"command": raw.strip(), "args": {}}
    response = handler.handle(request)
    print(response)