from Classes._status import Status

class Runtime:
    def __init__(self, services):
        self.services = services
        self.processes = {}

    def start(self):
        pass

    def stop(self):
        pass

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
