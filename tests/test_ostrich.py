import pytest
from ostrich import ostrich, Priority, mark_line
import io
import sys

def test_basic_decorator():
    @ostrich(Priority.HIGH)
    def test_func():
        return "test"
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    result = test_func()
    sys.stdout = sys.__stdout__
    
    # Check if function still works
    assert result == "test"
    # Check if output contains OSTRICH HIGH
    assert "[OSTRICH HIGH]" in captured_output.getvalue()

def test_ticket_reference():
    @ostrich(Priority.HIGH, "JIRA-123")
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    assert "[JIRA-123]" in captured_output.getvalue()

def test_line_marking():
    @ostrich(Priority.HIGH, lines={15: "Test comment"})
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    assert "Test comment" in captured_output.getvalue()

def test_context_manager():
    @ostrich(Priority.HIGH)
    def test_func():
        with mark_line("Test line mark"):
            return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    assert "Test line mark" in captured_output.getvalue()

def test_no_priority():
    @ostrich()
    def test_func():
        return "test"
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    test_func()
    sys.stdout = sys.__stdout__
    
    # Should have LOL priority and a random excuse
    assert "[OSTRICH LOL]" in captured_output.getvalue()

def test_all_priority_levels():
    for priority in Priority:
        @ostrich(priority)
        def test_func():
            return "test"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        test_func()
        sys.stdout = sys.__stdout__
        
        assert f"[OSTRICH {priority.name}]" in captured_output.getvalue()

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