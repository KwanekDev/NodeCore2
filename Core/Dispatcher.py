# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

class Dispatcher:
    def __init__(self, runtime):
        self.runtime = runtime


    def dispatch(self, request):
        _command = request.get("command")
        _args = request.get("args", {})

        self.routes = {
            "start": self.runtime.start,
            "stop": self.runtime.stop,
            "status": self.runtime.status
        }

        if _command in self.routes:
            return self.routes[_command]()
        
        return {"ok": False, "error": "unknown_command"}