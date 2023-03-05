import pytest
from pytemp import pytemp

ALLUNITS=['kelvin', 'fahrenheit', 'celsius']

class TestBasePytemp(object):
    """Base class for pytemp testing."""
    def test_celsius_to_all(self):
        expected_result = [283.15, 50.0]
        actual_result = []
        for unit in ALLUNITS:
            if unit != 'celsius':
                actual_result.append(pytemp(10,'celsius', unit))
        assert actual_result == expected_result

    def test_case_sensitivity(self):
        assert pytemp(18,'cElsius', 'Fahrenheit') == pytemp(18,'celsius', 'fahrenheit')

    def test_negative_kelvin_to_fahrenheit(self):
        assert -457.87 == pytemp(1,'kelvin', 'fahrenheit')
        assert "error" == pytemp(-1,'kelvin', 'fahrenheit')
        assert -439.87 == pytemp(11,'kelvin', 'fahrenheit')

    def test_plus_minus(self):
        assert pytemp(+5,'celsius', 'fahrenheit') == pytemp(5,'celsius', 'fahrenheit')
        assert pytemp(-0,'fahrenheit', 'kelvin') == pytemp(0,'fahrenheit', 'kelvin')
    def test_wrong_input(self):
        try:
            assert " " == pytemp("qwerty",'celsius', 'fahrenheit')
            assert False
        except SystemExit:
            assert True



