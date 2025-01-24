import functools
import inspect
from typing import Dict
from ostrich.constants import Priority
from ostrich.excuses import FUNNY_EXCUSES
import random
from ostrich.collector import OstrichCollector

def ostrich(priority=None, ticket=None, lines: Dict[int, str] = None):
    def decorator(func):
        func_source, func_start = inspect.getsourcelines(func)
        func_end = func_start + len(func_source)
        ostrich_line = func_start
        
        level = priority.name if isinstance(priority, Priority) else 'LOL'
        OstrichCollector.add(level, func.__name__, ostrich_line, ticket, lines)
        
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

            print(f"\n{color}{bold}═════════ OSTRICH {level} ════════{reset}")
            if ticket:
                print(f"{color}Location: Line {ostrich_line} [{ticket}]{reset}")
            else:
                excuse = random.choice(FUNNY_EXCUSES)
                print(f"{color}Location: Line {ostrich_line} - {excuse}{reset}")
            
            if lines:
                has_invalid_lines = any(line_num < func_start or line_num > func_end for line_num in lines.keys())
                if has_invalid_lines:
                    print(f"\n{color}{bold}🚨 WARNING{reset}")
                    print(f"{color}Function bounds: Lines {func_start}-{func_end}")
                    print(f"You can only mark lines within these bounds!{reset}")
                
                if any(0 <= line_num - func_start < len(func_source) for line_num in lines.keys()):
                    print(f"\n{color}{bold}📍 Marked Lines{reset}")
                    for line_num, comment in lines.items():
                        relative_line = line_num - func_start
                        if 0 <= relative_line < len(func_source):
                            marked_line = func_source[relative_line].strip()
                            print(f"{color}Line {line_num}: {comment}")
                            print(f"  → {marked_line}{reset}")

            print(f"{color}{bold}═════════════════════════════{reset}\n")
            return func(*args, **kwargs)
        return wrapper
    return decorator