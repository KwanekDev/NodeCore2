# Copyright 2026 Kwanek
#Licensed under the Apache License, Version 2.0

from pathlib import Path

from CLI.boostrap import create_app
from CLI.loop import run_loop

def main():
    base_dir = Path(__file__).parent
    config_path = base_dir / "config.toml"
    handler = create_app(base_dir)
    run_loop(handler, config_path)


if __name__ == "__main__":
    main()
