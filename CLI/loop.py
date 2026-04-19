from rich.console import Console 
from rich.prompt import Prompt

console = Console()

def run_loop(handler):
    def format_result(result: dict) -> str:
        return "\n".join(f"{k}: {v}" for k, v in result.items())

    while True:
        raw = Prompt.ask(">>>")
        parts = raw.strip().split()

        if not parts:
            continue

        _command = parts[0]
        _args = {}

        if len(parts) > 1: 
            _args["name"] = parts[1]

        request = {
            "command": _command,
            "args": _args
        }

        response = handler.handle(request)
        _msg = response.get("message")

        if _msg is not None:
            if isinstance(_msg, dict):
                console.print(format_result(_msg))
            else:
                console.print(_msg)