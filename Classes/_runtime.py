import subprocess
from Classes._status import Status

class Runtime:
    def __init__(self, services):
        self.services = services
        self.processes = {}

    def start(self):
        for name, cmd in self.services.items():
            proc = subprocess.Popen(cmd) 
            self.processes[name] = proc
        return {"ok": True, "message": f"Started {len(self.services)} services"}

    def stop(self):
        for proc in self.processes.values():
            proc.terminate()
        count = len(self.processes)
        self.processes.clear()
        return {"ok": True, "message": f"Stopped {count} services"}

    def status(self):
        if not self.processes:
            return {"ok": True, "message": "No services running. Call 'start' first."}
            
        result = {}
        for name, proc in self.processes.items():
            _processStatus = proc.poll()
            if _processStatus is None:
                result[name] = Status.ONLINE.value
            elif _processStatus == 0:
                result[name] = Status.OFFLINE.value
            else:
                result[name] = Status.ERROR.value
        return result
