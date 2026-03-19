import pytest
from app import IrrigationSystem

def test_irrigation_logic():
    logic = IrrigationSystem()
    
    # Test 1: Dry and hot -> Plenty of water
    assert logic.calculate_demand(20, 30) == "High"
    
    # Test 2: Moist enough -> No water
    assert logic.calculate_demand(70, 20) == "None"
    
    # Test 3: Invalid input -> Exception
    with pytest.raises(ValueError):
        logic.calculate_demand(-5, 20)