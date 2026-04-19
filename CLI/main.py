# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

from pathlib import Path
from Classes._runtime import Runtime
from Core.Requests import Requests
from Core.Dispatcher import Dispatcher


MODULES_DIR = Path("Examples")

def setup_services(dir):
    result = {}

    if dir.exists() and dir.is_dir():
        for script in dir.rglob("*.py"):
            if not script.name.startswith("_"):
                result[script.stem] = ["python", str(script)]

    return result

services = setup_services(MODULES_DIR)

runtime = Runtime(services)
dispatcher = Dispatcher(runtime)
handler = Requests(dispatcher)

while True:
    raw = input(">>> ")
    parts = raw.strip().split()

    if not parts:
        continue

    _command = parts[0]
    _args = {}

    if len(parts) > 1:
        _args["name"] = parts[1]
    
    request = {
        "command": _command,
        "args": _args
    }

    response = handler.handle(request)
    _msg = response.get("message")
    if _msg is not None:
        print(_msg)