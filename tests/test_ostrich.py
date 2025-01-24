import pytest
from ostrich import ostrich, Priority
import io
import sys

def test_basic_decorator():
    @ostrich(Priority.HIGH)
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    result = test_func()
    sys.stdout = sys.__stdout__
    
    assert result == "test"
    assert "OSTRICH HIGH" in captured_output.getvalue()

def test_ticket_reference():
    @ostrich(Priority.HIGH, "JIRA-123")
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    assert "[JIRA-123]" in captured_output.getvalue()

def test_no_priority():
    @ostrich()
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    assert "OSTRICH LOL" in captured_output.getvalue() 

def test_all_priority_levels():
    for priority in Priority:
        @ostrich(priority)
        def test_func():
            return "test"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        test_func()
        sys.stdout = sys.__stdout__
        
        assert f"OSTRICH {priority.name}" in captured_output.getvalue() 

def test_docstring_preservation():
    @ostrich(Priority.HIGH)
    def test_func():
        """Original docstring."""
        return "test"
    
    assert "Original docstring" in test_func.__doc__

def test_function_name_preservation():
    @ostrich(Priority.HIGH)
    def test_func():
        return "test"
    
    assert test_func.__name__ == "test_func"

def test_decorator_output(capsys):
    @ostrich(Priority.HIGH, "TICKET-123")
    def sample_function():
        return "test"
    
    result = sample_function()
    captured = capsys.readouterr()
    
    assert result == "test"
    assert "OSTRICH HIGH" in captured.out 
    assert "TICKET-123" in captured.out