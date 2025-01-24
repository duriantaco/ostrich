## src/ostrich/constants.py
from enum import Enum

class Priority(Enum):
    CRITICAL = '\033[91m'  # red
    HIGH = '\033[93m'      # yellow
    MEH = '\033[94m'       # blue
    LOW = '\033[92m'       # green
    LOL = '\033[90m'       # gray