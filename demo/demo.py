from ostrich import ostrich, Priority
from ostrich.collector import OstrichCollector

@ostrich(Priority.HIGH, "PERF-123", lines={
    7: "This loop is O(n) and slow af",
    8: "This is where everything breaks"
})
def slow_function():
        for i in range(1000000):  
            pass
        return "Done!"

@ostrich(Priority.MEH, lines={
    19: "Copy-pasted from StackOverflow at 3am"
})
def hehe_function():
        x = {'a': 1, 'b': 2}  
        return "Meh"

@ostrich(lines={
    23: "Legacy code from 1995",
    24: "We're too scared to touch this"
})
def yolo_function():
        result = "¯\_(ツ)_/¯" 
        return result

if __name__ == "__main__":
    print("\nRunning slow function:")
    print("-" * 50)
    slow_function()
    
    print("\nRunning meh function:")
    print("-" * 50)
    hehe_function()
    
    print("\nRunning yolo function:")
    print("-" * 50)
    yolo_function()

    OstrichCollector.report()