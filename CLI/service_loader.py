from pathlib import Path

def setup_services(dir: Path):
    result = {}

    if dir.exists() and dir.is_dir():
        for script in dir.rglob("*.py"):
            if not script.name.startswith("_"):
                result[script.stem] = ["python", str(script)]

    return result