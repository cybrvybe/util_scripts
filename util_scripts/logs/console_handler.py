# utils/console.py

from rich.console import Console
from rich.progress import Progress
from rich.logging import RichHandler
import logging

class ConsoleHandler:

    def get_console(self):
        return Console()
    
    def get_logger(self):
        console = self.get_console()
        logging.basicConfig(
            level="INFO",
            format="%(message)s",
            datefmt="[%X]",
            handlers=[RichHandler(console=console)],
        )

        logger = logging.getLogger("rich")
        return logger
    
    def get_progress(self):
        console = self.get_console()
        progress = Progress(console=console)
        return progress
