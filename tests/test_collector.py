import pytest
from ostrich.collector import OstrichCollector

def test_add_ostrich():
    OstrichCollector.instances = {
        'CRITICAL': [],
        'HIGH': [],
        'MEH': [], 
        'LOW': [],
        'LOL': []
    }
    
    OstrichCollector.add('CRITICAL', 'test_func', 10, 'TICKET-123', [10, 11])
    assert len(OstrichCollector.instances['CRITICAL']) == 1
    assert OstrichCollector.instances['CRITICAL'][0]['function'] == 'test_func'
    assert OstrichCollector.instances['CRITICAL'][0]['line'] == 10
    assert OstrichCollector.instances['CRITICAL'][0]['ticket'] == 'TICKET-123'
    assert OstrichCollector.instances['CRITICAL'][0]['marked_lines'] == [10, 11]

def test_report_no_ostriches(capsys):
    OstrichCollector.instances = {
        'CRITICAL': [],
        'HIGH': [],
        'MEH': [], 
        'LOW': [],
        'LOL': []
    }
    
    OstrichCollector.report()
    captured = capsys.readouterr()
    assert "No ostriches found! Your code is either perfect or you're in denial." in captured.out

def test_report_with_ostriches(capsys):
    OstrichCollector.instances = {
        'CRITICAL': [],
        'HIGH': [],
        'MEH': [], 
        'LOW': [],
        'LOL': []
    }
    
    OstrichCollector.add('CRITICAL', 'test_func', 10, 'TICKET-123', [10, 11])
    OstrichCollector.add('LOW', 'another_func', 20)
    
    OstrichCollector.report()
    captured = capsys.readouterr()
    
    assert "CRITICAL Priority: 1 ostrich" in captured.out
    assert "test_func at line 10 [TICKET-123]" in captured.out
    assert "2 marked lines" in captured.out
    
    assert "LOW Priority: 1 ostrich" in captured.out
    assert "another_func at line 20" in captured.out
    
    assert "Total Ostriches: 2" in captured.out
    assert "Total Marked Lines: 2" in captured.out