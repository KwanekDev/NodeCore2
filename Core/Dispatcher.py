# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

class Dispatcher:
    def __init__(self, runtime):
        self.runtime = runtime

    def dispatch(self, request):
        _command = request.get("command")
        _args = request.get("args", {})

        if _command == "start":
            self.runtime.start()
            return {"ok": True}
        
        if _command == "stop":
            self.runtime.stop()
            return {"ok": False}
        
        if _command == "status":
            return {"ok": True, "data": self.runtime.status()}
        
        return {"ok": False, "error": "unknown_command"}