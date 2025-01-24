# 🙈 Ostrich Problems

A useless Python package for marking technical debt in your codebase. Based on the infamous "Ostrich Algorithm" - if you can't see the problem, is it really a problem? As the saying usually goes, if you don't see it, it's not there /s. 

## WTF is the Ostrich Algorithm?

The Ostrich Algorithm is a term in programming where developers deliberately ignore certain problems in their code (like an ostrich "burying its head in the sand"). While it sounds like a joke, it's actually a legitimate strategy when:

- The problem is super unlikely to occur (or at least we hope so)
- Fixing it would cost more than ignoring it 
- You're dealing with legacy code that works (don't touch it ever!)
- Your deadline was yesterday

This package turns this concept into a (hopefully) useful marking system for your code, letting you:
- Flag problematic code with priority levels
- Add ticket references
- Get reminded of your poor life choices with random funny messages
- Make your technical debt visible (but still ignore it professionally)

## Installation

```bash
pip install ostrich-problems
```

## Quick Start

```python
from ostrich import ostrich, Priority, mark_line

# mark high priority issues with specific line problems
@ostrich(Priority.HIGH, "JIRA-123", lines={
    15: "This regex makes senior devs cry",
    20: "O(n³) but we pretend it's O(1)"
})
def slow_as_hell_function():
    print("This function is slower than my career progress...")
    with mark_line("This loop needs Jesus"):
        for i in range(1000):  # this line will be marked
            do_something_terrible(i)
    return "somehow it worked"

# mark medium priority stuff you'll "fix later"
@ostrich(Priority.MEH)
def might_explode():
    with mark_line("Copy pasted from a 2009 forum"):
        legacy_code_block()
    return "🤞"

# ignore it with style (gets random funny excuse)
@ostrich()
def pure_chaos():
    with mark_line("Nobody remembers what this does"):
        important_business_logic()
    return "¯\_(ツ)_/¯"
```

## Real world example

```python
from ostrich import ostrich, Priority, mark_line

# Mark performance issues
@ostrich(Priority.HIGH, "PERF-123", lines={
    15: "This query makes the DB cry",
    22: "N+1 query problem but it's Friday"
})
def calculate_user_metrics():
    results = []
    with mark_line("O(n²) loop that we'll fix 'later'"):
        for user in all_users:         # Line will be marked
            for metric in all_metrics:  # This is fine 🔥
                results.append(calculate_metric(user, metric))
    return results

# Mark sketchy code
@ostrich(Priority.MEH)
def cleanup_data():
    with mark_line("This regex was written at 3am"):
        pattern = r'^[^\s]{0,}(?<=\w{3})\d+'  # Line will be marked
    return "Cleaned(ish)!"

# Output will look like:
# [OSTRICH HIGH][PERF-123]  <- in yellow
# Marked lines in this function:
# Line 15: This query makes the DB cry
# -> query = "SELECT * FROM users WHERE..."
# Line 22: N+1 query problem but it's Friday
# -> for metric in all_metrics:
# -> This loop needs Jesus <- from context manager
```

## When to Use This?

1. You've got some hacky code that works but needs attention later
2. You want to track technical debt in a fun way
3. You need to mark priority levels for future fixes
4. Your code review involves a lot of "we'll fix it later"
5. Or you want to live in self-denial

## Contributing

Found a bug? (Or want to professionally ignore it?) Feel free to:
- Add more funny excuses
- Suggest new priority levels
- Report bugs (or ignore them, staying true to the spirit)
- Improve documentation (or don't, who reads docs anyway?)

## Why Use This?

Because sometimes you need to:
1. Track technical debt without crying
2. Make your team laugh about bad code instead of quitting
3. Show management exactly how many problems you're "working on"
4. Turn your shame into a feature

## Disclaimer

This is meant to be a joke. Please write proper code. 

## License

MIT License - Because we take some responsibility (unlike our code)
