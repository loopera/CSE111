from wetflag_calculator import calculate_weight, \
    calculate_energy, \
    calculate_tube_size, \
    calculate_fluids, \
    calculate_adrenaline_dose, \
    calculate_glucose_dose

import pytest
from pytest import approx

def test_calculate_weight():
    assert calculate_weight(1) == approx (10, abs = 0.001)
    assert calculate_weight(2) == approx (12, abs = 0.001)
    
    assert calculate_weight(16) == approx (40, abs = 0.001)

def test_calculate_energy():
    assert calculate_energy(10) == approx (40, abs = 0.001)
    assert calculate_energy(20) == approx (80, abs = 0.001)
    assert calculate_energy(40) == approx (160, abs = 0.001)


def test_calculate_tube_size():
    assert calculate_tube_size(1) == approx (4.25, abs = 0.001)
    assert calculate_tube_size(4) == approx (5.00, abs = 0.001)
    assert calculate_tube_size(7) == approx (5.75, abs = 0.001)

def test_calculate_fluids():
    assert calculate_fluids(25) == approx (500, abs = 0.001)
    assert calculate_fluids(30) == approx (600, abs = 0.001)
    assert calculate_fluids(15) == approx (300, abs = 0.001)

def test_calculate_adrenaline_dose():
    assert calculate_adrenaline_dose(10) == approx (1, abs = 0.001)
    assert calculate_adrenaline_dose(20) == approx (2, abs = 0.001)
    assert calculate_adrenaline_dose(35) == approx (3.5, abs = 0.001)

def test_calculate_glucose_dose():
    assert calculate_glucose_dose(15) == approx (30, abs = 0.001)
    assert calculate_glucose_dose(30) == approx (60, abs = 0.001)
    assert calculate_glucose_dose(37) == approx (74, abs = 0.001)



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
