# utils/handlers.py

from util_scripts.logs.console_handler import ConsoleHandler
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as rprint
from typing import Any

class LogHandler:
    def __init__(self):
        self.console_handler = ConsoleHandler()
        self.logger = self.console_handler.get_logger()
        self.console = self.console_handler.get_console()
        self.progress = self.console_handler.get_progress()

    def log_info(self, message: str):
        self.logger.info(message)


    def log_error(self, message: str):
        self.logger.error(message)


    def log_warning(self, message: str):
        self.logger.warning(message)


    def print_error(self, message: str):
        self.console.print(f"[bold red]{message}[/bold red]")


    def print_success(self, message: str):
        self.console.print(f"[bold green]{message}[/bold green]")


    def print_info(self, message: str):
        self.console.print(f"[bold blue]{message}[/bold blue]")


    def start_progress_task(self, total: int, description: str = "") -> Any:
        return self.progress.add_task(description, total=total)


    def update_progress(self, task_id: Any, advance: int = 1):
       return self.progress.update(task_id, advance=advance)


    def prompt_input(self, text: str) -> str:
        return Prompt.ask(text)


    def confirm_action(self, text: str) -> bool:
        return Prompt.confirm(text)


    def pretty_print(self, text: str):
        rprint(Panel(text))
