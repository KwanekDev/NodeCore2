import subprocess
from Classes._status import Status

class Runtime:
    def __init__(self, services):
        self.services = services
        self.processes = {}

    def start(self):
        for name, cmd in self.services.items():
            proc = subprocess.Popen(cmd, shell=False)
            self.processes[name] = proc

    def stop(self):
        for proc in self.processes.values():
            proc.terminate()
        self.processes.clear()

    def status(self):
        result = {}

        for name, proc in self.processes.items():
            _processStatus = proc.poll()
            if _processStatus is None:
                result[name] = Status.ONLINE
            elif _processStatus is 0:
                result[name] = Status.OFFLINE
            else:
                result[name] = Status.ERROR
