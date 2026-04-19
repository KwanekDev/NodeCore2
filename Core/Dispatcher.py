# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

class Dispatcher:
    def __init__(self, runtime):
        self.runtime = runtime
        self.routes = {
            "start": self.runtime.start,
            "stop": self.runtime.stop,
            "status": self.runtime.status
        }

    def dispatch(self, request):
        _command = request.get("command")
        _args = request.get("args", {})

        handler = self.routes.get(_command)
        if not handler:
            return {"ok": False, "message": "unknown_command"}
        try:
            return handler(**_args)
        except TypeError:

            return {"ok": False, "message": "Fatal error"}