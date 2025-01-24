# src/ostrich/__init__.py
from .core import ostrich
from .constants import Priority
from .collector import OstrichCollector

__all__ = ['ostrich', 'Priority', 'OstrichCollector']