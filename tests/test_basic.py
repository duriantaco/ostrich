# tests/test_basic.py
def test_import():
    from ostrich import ostrich, Priority
    assert ostrich is not None
    assert Priority is not None
