# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

class Requests:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def handle(self, request):
        if not isinstance(request, dict):
            return {"ok": False, "message": "invalid_request"}
        
        if "command" not in request:
            return {"ok": False, "message": "missing_command"}
        
        return self.dispatcher.dispatch(request)