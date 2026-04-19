# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

class Requests:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def handle(self, request):
        if not isinstance(request, dict):
            return {"ok": False, "message": "invalid_request"}
        
        _command = request.get("command")

        if not _command:
            return {"ok": False, "message": "missing_command"}
        
        _service = request.get("service")
        return self.dispatcher.dispatch(request)