def test_voltage(voltage):
    min_voltage = 4.75
    max_voltage = 5.25

    if voltage < min_voltage:
        result = "FAIL"
        reason = "Voltage is below minimum"
    elif voltage > max_voltage:
        result = "FAIL"
        reason = "Voltage is above maximum"
    else:
        result = "PASS"
        reason = "Voltage is within the acceptable range"


    print("Test: Voltage")
    print(f"Measured: {voltage:.2f} V")
    print(f"Allowed Range: {min_voltage:.2f}-{max_voltage:.2f} V")
    print("Result:", result)
    print("Reason:", reason)

reading = 5.21
test_voltage(reading)