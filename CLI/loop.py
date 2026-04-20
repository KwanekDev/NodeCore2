import time
from datetime import timedelta, datetime
from rich.console import Console, Group
from rich.prompt import Prompt
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()

def show_banner(config_path=None):
    project_name = "NodeCore"
    if config_path:
        try:
            import tomllib
            with open(config_path, "rb") as f:
                config = tomllib.load(f)
                project_name = config.get("Path", "NodeCore")
        except:
            pass

    header_info = Text.from_markup(
        "[link=https://github.com/KwanekDev/NodeCore2]★ GitHub[/link]  [dim #78350f]•[/]  558cf09"
    )
    
    welcome_panel = Panel(
        Text(f"NodeCore 2", style="bold #facc15"),
        border_style="#b45309",
        expand=False,
        box=box.ROUNDED
    )

    ascii_lines = [
        "███╗   ██╗ ██████╗ ██████╗ ███████╗",
        "████╗  ██║██╔═══██╗██╔══██╗██╔════╝",
        "██╔██╗ ██║██║   ██║██║  ██║█████╗  ",
        "██║╚██╗██║██║   ██║██║  ██║██╔══╝  ",
        "██║ ╚████║╚██████╔╝██████╔╝███████╗",
        "╚═╝  ╚═══╝ ╚═════╝ ╚═════╝ ╚══════╝",
        " ██████╗ ██████╗ ██████╗ ███████╗  ",
        "██╔════╝██╔═══██╗██╔══██╗██╔════╝  ",
        "██║     ██║   ██║██████╔╝█████╗    ",
        "██║     ██║   ██║██╔══██╗██╔══╝    ",
        "╚██████╗╚██████╔╝██║  ██║███████╗  ",
        " ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝  "
    ]

    logo_text = Text()
    gradient_colors = [
        "#b6851c", "#9b720a", "#c07f34", "#d97706",
        "#c48759", "#c28229", "#d89d4f", "#c48d3c",
        "#c98c3c", "#d97706", "#c08253", "#b8853e"
    ]
    for line, color in zip(ascii_lines, gradient_colors):
        logo_text.append(line + "\n", style=f"bold {color}")

    commands_menu = Text()
    commands_menu.append("Available Commands:\n", style="bold #facc15")
    commands_menu.append("  status  ", style="bold #facc15")
    commands_menu.append("[name] <True/False>  - Check node status (detailed info with True/False)\n", style="dim #fde68a")
    commands_menu.append("  start   ", style="bold #facc15")
    commands_menu.append("<name>               - Start a specific node\n", style="dim #fde68a")
    commands_menu.append("  stop    ", style="bold #facc15")
    commands_menu.append("<name>               - Stop a specific node\n", style="dim #fde68a")
    commands_menu.append("  help    ", style="bold #facc15")
    commands_menu.append("                      - Show detailed documentation", style="dim #fde68a")

    main_group = Group(
        header_info,
        Text(""), 
        welcome_panel,
        logo_text,
        commands_menu
    )

    banner = Panel(
        main_group,
        border_style="#b45309",
        padding=(1, 4),
        expand=False,
        box=box.ROUNDED
    )

    console.print("\n")
    console.print(Align.center(banner))
    console.print("\n") 

def run_loop(handler, config_path=None):
    def format_result(result: dict, indent=0) -> str:
        lines = []
        for k, v in result.items():
            prefix = "  " * indent
            if isinstance(v, dict):
                if "status" in v:
                    started_at = v.get("started_at")
                    if started_at:
                        dt = datetime.fromtimestamp(started_at).strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        dt = "N/A"
                    status_val = v.get('status', 'N/A')
                    status_color = "#10b981" if status_val == "Online" else "#ef4444" if status_val == "Error" else "#6b7280"
                    
                    lines.append(f"{prefix}[bold #facc15]{k}[/]")
                    lines.append(f"{prefix}  status  [dim #a16207]→[/] [{status_color}]{status_val}[/]")
                    lines.append(f"{prefix}  pid     [dim #a16207]→[/] [#facc15]{v.get('pid', 'N/A')}[/]")
                    if v.get('code') is not None:
                        lines.append(f"{prefix}  code    [dim #a16207]→[/] [#facc15]{v.get('code')}[/]")
                    lines.append(f"{prefix}  started [dim #a16207]→[/] [#facc15]{dt}[/]")
                else:
                    lines.append(f"{prefix}[bold #facc15]{k}[/]")
                    lines.extend(format_result(v, indent+1).split("\n"))
            else:
                status_color = "#10b981" if v == "Online" else "#ef4444" if v == "Error" else "#6b7280"
                color = status_color if v in ["Online", "Error", "Offline"] else "#facc15"
                lines.append(f"{prefix}[bold #facc15]{k}[/] [dim #a16207]→[/] [{color}]{v}[/]")
        return "\n".join(lines)

    show_banner(config_path)
    
    while True:
        raw = Prompt.ask("[bold #f97316]❯[/]")
        parts = raw.strip().split()

        if not parts:
            continue

        _command = parts[0].lower()
        
        if _command == "help":
            help_text = Text()
            help_text.append("NodeCore 2 - Service Manager\n\n", style="bold #facc15")
            help_text.append("Commands:\n", style="bold #facc15")
            help_text.append("  status [name] [true/false]\n", style="#fbbf24")
            help_text.append("    Check node status. Add 'true' for detailed info.\n\n", style="dim #fde68a")
            help_text.append("  start <name>\n", style="#10b981")
            help_text.append("    Start a specific node.\n\n", style="dim #fde68a")
            help_text.append("  stop <name>\n", style="#ef4444")
            help_text.append("    Stop a specific node.\n\n", style="dim #fde68a")
            help_text.append("  help\n", style="#fbbf24")
            help_text.append("    Show this help message.", style="dim #fde68a")
            
            console.print(help_text)
            console.print()
            continue

        _args = {}

        if len(parts) > 1: 
            if _command == "status":
                for arg in parts[1:]:
                    if arg.lower() == "true":
                        _args["detailed"] = True
                    elif arg.lower() == "false":
                        _args["detailed"] = False
                    else:
                        _args["name"] = arg
            else:
                _args["name"] = parts[1]

        request = {
            "command": _command,
            "args": _args
        }

        try:
            response = handler.handle(request)
            _msg = response.get("message")
        except Exception as e:
            _msg = f"[red]Error: {e}[/]"

        if _msg is not None:
            if isinstance(_msg, dict):
                console.print(format_result(_msg))
            else:
                console.print(_msg)
        
        console.print()