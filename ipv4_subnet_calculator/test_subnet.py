import pytest

from subnet_calculator import calculate_subnet

def test_basic_subnet():
    result = calculate_subnet("192.168.1.10", 24)

    assert str(result["Network Address"]) == "192.168.1.0"
    assert str(result["Broadcast Address"]) == "192.168.1.255"
    assert result["Usable Hosts"] == 254


def test_class_b_subnet():
    result = calculate_subnet("172.16.5.20", 16)

    assert str(result["Network Address"]) == "172.16.0.0"
    assert str (result["Broadcast Address"]) == "172.16.255.255"
    assert result["Usable Hosts"] == 65534

def test_class_a_subnet():
    result = calculate_subnet("10.0.0.5", 8)

    assert str(result["Network Address"]) == "10.0.0.0"
    assert str(result["Broadcast Address"]) == "10.255.255.255"
    assert result["Usable Hosts"] == 16777214

def test_invalid_ip():
    with pytest.raises(ValueError):
        calculate_subnet("192.168.1.300", 24)

def test_invalid_prefix():
    with pytest.raises(ValueError):
        calculate_subnet("192.168.1.10", 33)

def test_point_to_point_subnet():
    result = calculate_subnet("192.168.1.10", 31)
    assert result["Usable Hosts"] == 2

def test_single_host_subnet():
    result = calculate_subnet("192.168.1.10", 32)
    assert result["Usable Hosts"] == 1