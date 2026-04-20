import subprocess
import time
from Classes._status import Status

class Runtime:
    def __init__(self, services):
        self.services = services
        self.processes = {}

    def start(self, name=None):
        if name:
            if name in self.services:
                proc = subprocess.Popen(self.services[name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                self.processes[name] = {
                    "proc": proc,
                    "started_at": time.time()
                }
                return {"ok": True, "message": f"Started {name}"}
            return {"ok": False, "message": f"Service {name} not found"}

        for name, cmd in self.services.items():
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) 
            self.processes[name] = {
                "proc": proc,
                "started_at": time.time()
            }
        return {"ok": True, "message": f"Started {len(self.services)} services"}

    def stop(self, name=None):
        if name:
            proc = self.processes.get(name)
            if not proc:
                return {"ok": False, "message": f"Service {name} not running"}

            proc["proc"].terminate()
            del self.processes[name]
            return {"ok": True, "message": f"Stopped {name}"}

        for proc in self.processes.values():
            proc["proc"].terminate()
        count = len(self.processes)
        self.processes.clear()
        return {"ok": True, "message": f"Stopped {count} services"}

    def status(self, name=None, detailed=False):
        result = {}

        targets = [name] if name else list(self.services.keys())

        for svc_name in targets:
            _proc = self.processes.get(svc_name)

            if _proc:
                _processStatus = _proc["proc"].poll()

                if _processStatus is None:
                    _status = Status.ONLINE.value
                elif _processStatus == 0:
                    _status = Status.OFFLINE.value
                else:
                    _status = Status.ERROR.value

                if detailed:
                    result[svc_name] = {
                        "status": _status,
                        "pid": _proc["proc"].pid,
                        "code": _processStatus,
                        "started_at": _proc["started_at"]
                    }
                else:
                    result[svc_name] = _status
            else:
                if detailed:
                    result[svc_name] = {
                        "status": Status.OFFLINE.value,
                        "pid": 0,
                        "code": None,
                        "started_at": None
                    }
                else:
                    result[svc_name] = Status.OFFLINE.value
                
        return {"ok": True, "message": result}