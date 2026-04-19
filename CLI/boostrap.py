# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

from pathlib import Path
import tomllib

from Classes._runtime import Runtime
from Core.Requests import Requests
from Core.Dispatcher import Dispatcher
from .service_loader import setup_services

def load_config(config_path: Path):
    if not config_path.exists():
        return {"ok": False, "message": "config not found"}
    
    with open(config_path, "rb") as con:
        return tomllib.load(con)
    
def resolve_root_dir(start: Path):
    return start.parent

def create_app(base_dir: Path):
    config_path = base_dir / "config.toml"
    config = load_config(config_path)
    proj_path = config.get("Path")

    root_dir = resolve_root_dir(base_dir)
    modules_dir = root_dir / proj_path
    services = setup_services(modules_dir)



    # do not touch
    runtime = Runtime(services)
    dispatcher = Dispatcher(runtime)
    handler = Requests(dispatcher)

    return handler

