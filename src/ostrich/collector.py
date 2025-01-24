# src/ostrich/collector.py
from .constants import Priority

class OstrichCollector:
   """Collects all ostrich instances and their priorities"""
   instances = {
       'CRITICAL': [],
       'HIGH': [],
       'MEH': [], 
       'LOW': [],
       'LOL': []
   }
   
   @classmethod
   def add(cls, level, func_name, line, ticket=None, marked_lines=None):
       cls.instances[level].append({
           'function': func_name,
           'line': line,
           'ticket': ticket,
           'marked_lines': marked_lines
       })
   
   @classmethod 
   def report(cls):
       print("\n🦘 OSTRICH REPORT 🦘")
       print("=" * 50)
       
       total = sum(len(ostriches) for ostriches in cls.instances.values())
       if total == 0:
           print("No ostriches found! Your code is either perfect or you're in denial.")
           return
           
       # show all levels even if empty
       for level, ostriches in cls.instances.items():
           color = Priority[level].value if level in Priority.__members__ else '\033[0m'
           reset = '\033[0m'
           bold = '\033[1m'
           
           count = len(ostriches)
           print(f"{color}{bold}{level} Priority: {count} ostrich{'es' if count != 1 else ''}{reset}")
           
           if ostriches:  
               for o in ostriches:
                   ticket_info = f" [{o['ticket']}]" if o['ticket'] else ""
                   print(f"{color}  • {o['function']} at line {o['line']}{ticket_info}")
                   if o['marked_lines']:
                       print(f"    {len(o['marked_lines'])} marked line{'s' if len(o['marked_lines']) > 1 else ''}{reset}")
           print()
           
       print("=" * 50)
       print(f"Total Ostriches: {total}")
       marked_lines = sum(
           len(o['marked_lines'] or []) 
           for ostriches in cls.instances.values() 
           for o in ostriches
       )
       print(f"Total Marked Lines: {marked_lines}\n")