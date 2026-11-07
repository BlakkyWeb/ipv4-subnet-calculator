import math

def test_parameter(name, value, minimum, maximum, unit):
    if value is None or isinstance(value, bool):
        return {
            "name": name,
            "value": value,
            "unit": unit,
            "result": "INVALID",
            "reason": "Missing or invalid measurement."
        }
    try:
        value = float(value)
    except (ValueError, TypeError):
        return {
            "name": name,
            "value": value,
            "unit": unit,
            "result": "INVALID",
            "reason": "Measurement must be numeric."
        }
    if not math.isfinite(value):
        return {
            "name": name,
            "value": value,
            "unit": unit,
            "result": "INVALID",
            "reason": "Measurement must be finite."
        }

    if value < minimum:
        result = "FAIL"
        reason = "Below minimum limit."

    elif value > maximum:
        result = "FAIL"
        reason = "Above acceptable limit."

    else:
        result = "PASS"
        reason = "Within acceptable range"


    return {
        "name": name,
        "value": value,
        "unit": unit,
        "result": result,
        "reason": reason
    }

def test_device(device):
    specifications = {
        "voltage": (4.75, 5.25, "V"),
        "current": (0.00, 0.50, "A"),
        "resistance": (90.0, 110.0, "ohm")
    }

    results = []

    for parameter, limits in specifications.items():
        maximum, minimum, unit = limits

        result = test_parameter(
            parameter.capitalize(),
            device.get(parameter),
            minimum,
            maximum,
            unit
        )

        results.append(result)

        if all(test["result"] == "PASS" for test in results):
            overall = "PASS"
        else:
            overall = "FAIL"

        return {
            "device_id": device["id"],
            "results": results,
            "overall": overall
        }

devices = [
    {
        "id":"DEV-001",
        "voltage": 5.00,
        "current": 0.30,
        "resistance": 100
    },
    {
        "id": "DEV-002",
        "voltage": 5.40,
        "current": 0.30,
        "resistance": 100
    },
    {
        "id": "DEV-003",
        "voltage": 5.00,
        "current": 0.60,
        "resistance": 85
    }
]

batch_results = []

for device in devices:
    report = test_device(device)
    batch_results.append(report)

print('==' * 25)
print("AUTOMATED EQUIPMENT BATCH TEST REPORT")
print('==' * 25)

for report in batch_results:
    print(f"\nDevice: {report['device_id']}")

    for test in report["results"]:
        value = test["value"]

        if test["result"] == "INVALID":
            measured = repr(value)
        else:
            measured = f"{value:.2f} {test['unit']}"

        print(
            f"{test['name']}: {measured} | "
            f"{test['result']} | {test['unit']}"
        )

    print(f"OVERALL: {report['overall']}")


passed = sum(
    report["overall"] == "PASS"
    for report in batch_results
)

failed = len(batch_results) - passed

print("\n" + "=" * 35)
print("BATCH SUMMARY")
print(f"Devices tested: {len(batch_results)}")
print(f"Devices passed: {passed}")
print(f"Devices failed: {failed}")
print("=" *35)