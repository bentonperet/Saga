"""
Simple validation test without Unicode emojis (Windows compatible)
"""

from pachyderm_schema_validator import validate_metadata

print("=" * 80)
print("VALIDATION TEST")
print("=" * 80)

is_valid, alerts = validate_metadata("pachyderm_metadata.json")

if alerts:
    print(f"\nFound {len(alerts)} alert(s):\n")

    errors = [a for a in alerts if a.severity == "ERROR"]
    warnings = [a for a in alerts if a.severity == "WARNING"]
    infos = [a for a in alerts if a.severity == "INFO"]

    print(f"ERRORS: {len(errors)}")
    print(f"WARNINGS: {len(warnings)}")
    print(f"INFO: {len(infos)}")
    print()

    if errors:
        print("-" * 80)
        print("ERRORS:")
        print("-" * 80)
        for alert in errors:
            print(f"\n[{alert.component}] {alert.message}")
            if alert.recommendation:
                print(f"  Fix: {alert.recommendation}")

    if warnings:
        print("\n" + "-" * 80)
        print("WARNINGS:")
        print("-" * 80)
        for alert in warnings:
            print(f"\n[{alert.component}] {alert.message}")
            if alert.recommendation:
                print(f"  Recommendation: {alert.recommendation}")

    if infos:
        print("\n" + "-" * 80)
        print("INFO:")
        print("-" * 80)
        for alert in infos:
            print(f"\n[{alert.component}] {alert.message}")

else:
    print("\nNo issues found - validation passed!")

print("\n" + "=" * 80)
if is_valid:
    print("Status: PASSED" + (" WITH WARNINGS" if alerts else ""))
else:
    print("Status: FAILED")
print("=" * 80)
