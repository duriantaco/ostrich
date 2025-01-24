import functools
import inspect
from contextlib import contextmanager
from typing import Dict
from .constants import Priority
from .excuses import FUNNY_EXCUSES
import random

def ostrich(priority=None, ticket=None, lines: Dict[int, str] = None):
    """
    A decorator that marks code with priority levels and specific line comments.
    
    Args:
        priority (Priority, optional): Priority level from the Priority enum
        ticket (str, optional): Ticket reference (e.g., "JIRA-123")
        lines (Dict[int, str], optional): Dictionary of line numbers and their comments
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(priority, Priority):
                color = priority.value
                level = priority.name
            else:
                color = Priority.LOL.value
                level = "LOL"

            reset = '\033[0m'
            bold = '\033[1m'

            if ticket:
                header = f"{color}{bold}# [OSTRICH {level}][{ticket}]{reset}"
            else:
                header = f"{color}{bold}# [OSTRICH {level}]{reset}"

            if priority is None:
                excuse = random.choice(FUNNY_EXCUSES)
                header += f" {excuse}"

            print(header)

            source_lines, start_line = inspect.getsourcelines(func)
            
            if lines:
                print(f"{color}# Marked lines in this function:{reset}")
                for line_num, comment in lines.items():
                    rel_line = line_num - start_line
                    if 0 <= rel_line < len(source_lines):
                        print(f"{color}# Line {line_num}: {comment}")
                        print(f"# -> {source_lines[rel_line].strip()}{reset}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

class LineMarker:
    def __init__(self):
        self._current_comment = None
        
    @contextmanager
    def mark(self, comment: str):
        """Context manager for marking specific lines of code."""
        prev_comment = self._current_comment
        self._current_comment = comment
        try:
            frame = inspect.currentframe().f_back
            if self._current_comment:
                print(f"\033[93m# -> Line {frame.f_lineno}: {self._current_comment}\033[0m")
            yield
        finally:
            self._current_comment = prev_comment

mark_line = LineMarker().mark