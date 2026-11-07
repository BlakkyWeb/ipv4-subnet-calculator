def test_parameter(name, value, minimum, maximum, unit):
    if value < minimum:
        result = "FAIL"
        reason = f"{name} is below the minimum limit"
    elif value > maximum:
        result = "FAIL"
        reason = f"{name} is above the maximun limit"
    else:
        result = "PASS"
        reason = f"{name} is within the acceptable limit"

    return {
        "name": name,
        "value": value,
        "minimum": minimum,
        "maximum": maximum,
        "unit": unit,
        "result": result,
        "reason": reason
    }

voltage = 5.0
current = 0.47
resistance = 95.0

results = [
    test_parameter("voltage", voltage, 4.75, 5.25, "V"),
    test_parameter("current", current, 0.00, 0.50, "A"),
    test_parameter("Resistance", resistance, 90.0, 110.0, "ohm")
]

print("-" * 45)
print("EQUIPMENT TEST REPORT")
print("-" * 45)

for test in results:
    print(f"\nTest: {test['name']}")
    print(f"Measured: {test['value']:.2f} {test['unit']}")
    print(
        f"Allowed range: {test['minimum']:.2f} - {test['maximum']:.2f} {test['unit']}"
    )
    print(f"Result: {test['result']}")
    print(f"Reason: {test['reason']}")


overall_result = (
    "PASS"
    if all(test['result'] == "PASS" for test in results)
    else "FAIL"
    )

print("\n" + "=" * 45)
print(f"OVERALL EQUIPMENT RESULT: {overall_result}")
print("=" * 45)