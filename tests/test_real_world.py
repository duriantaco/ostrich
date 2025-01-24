# tests/test_real_world.py
from ostrich import ostrich, Priority

def test_decorator_output(capsys):
    @ostrich(Priority.HIGH, "TICKET-123")
    def sample_function():
        return "test"
    
    result = sample_function()
    captured = capsys.readouterr()
    
    assert result == "test"
    assert "OSTRICH HIGH" in captured.out 
    assert "TICKET-123" in captured.out
