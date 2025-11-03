"""
PACHYDERM GLOBAL - Electrical Model Metadata Validator
Strict JSON schema validation with alerts and recommendations.
Generates validation_report.txt for QA traceability.
"""

import json
import jsonschema
from datetime import datetime
from pathlib import Path


# JSON Schema Definition
PACHYDERM_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "PACHYDERM Electrical Model Metadata",
    "description": "Tier III/IV Data Center Electrical System Model",
    "type": "object",
    "properties": {
        "topology": {
            "type": "string",
            "enum": ["radial", "dual", "ring", "distributed_redundant"],
            "description": "System topology type"
        },
        "generators": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "bus": {"type": "string"},
                    "type": {"enum": ["RECIP", "TURBINE"]},
                    "fuel": {"type": "string"},
                    "kw": {"type": "number", "minimum": 0},
                    "kva": {"type": "number", "minimum": 0}
                },
                "required": ["id", "type", "fuel", "kw", "kva"],
                "additionalProperties": True
            }
        },
        "transformers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "hv_bus": {"type": "string"},
                    "lv_bus": {"type": "string"},
                    "hv_voltage": {"type": "number", "minimum": 0},
                    "lv_voltage": {"type": "number", "minimum": 0},
                    "rated_s": {"type": "number", "minimum": 0}
                },
                "required": ["id", "hv_bus", "lv_bus", "rated_s"]
            }
        },
        "ups": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "bus": {"type": "string"},
                    "type": {"enum": ["STATIC", "ROTARY", "HYBRID"]},
                    "battery": {"enum": ["VRLA", "LI-ION", "NICD", "FLYWHEEL"]},
                    "function": {"enum": ["IT", "MECHANICAL", "CONTROL"]},
                    "kw": {"type": "number", "minimum": 0},
                    "kva": {"type": "number", "minimum": 0}
                },
                "required": ["id", "type", "battery", "function", "kw", "kva"]
            }
        },
        "mv_swbd": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "voltage": {"type": "number", "minimum": 0},
                    "rating_a": {"type": "number", "minimum": 0},
                    "interrupt_rating_ka": {"type": "number", "minimum": 0},
                    "redundancy": {"type": "string"},
                    "feeds": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["id", "voltage", "rating_a", "interrupt_rating_ka", "redundancy"]
            }
        },
        "lv_swbd": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "voltage": {"type": "number", "minimum": 0},
                    "rating_a": {"type": "number", "minimum": 0},
                    "interrupt_rating_ka": {"type": "number", "minimum": 0},
                    "redundancy": {"type": "string"},
                    "feeds": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["id", "voltage", "rating_a", "interrupt_rating_ka", "redundancy"]
            }
        },
        "earthing_tx": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "type": {"enum": ["ZIG-ZAG", "WYE-DELTA", "RESISTOR-GROUNDED"]},
                    "rated_kva": {"type": "number", "minimum": 0},
                    "impedance": {
                        "type": "object",
                        "properties": {
                            "r_ohm": {"type": "number"},
                            "x_ohm": {"type": "number"}
                        },
                        "required": ["r_ohm", "x_ohm"]
                    },
                    "neutral_resistance_ohm": {"type": "number"},
                    "connected_bus": {"type": "string"},
                    "grounding_connection": {
                        "type": "object",
                        "properties": {
                            "type": {"enum": ["RESISTIVE", "SOLID"]},
                            "neutral_to_ground_path": {"type": "string"},
                            "connection_impedance": {"type": "string"},
                            "ground_bus": {"type": "string"}
                        },
                        "required": ["type", "ground_bus"]
                    },
                    "z_matrix_3ph": {"type": "array"}
                },
                "required": ["id", "type", "rated_kva", "impedance", "connected_bus", "grounding_connection"]
            }
        }
    },
    "required": ["topology"]
}


class ValidationAlert:
    """Represents a validation alert with severity and recommendation."""
    
    def __init__(self, severity, component, field, message, recommendation):
        self.severity = severity  # 'ERROR', 'WARNING', 'INFO'
        self.component = component
        self.field = field
        self.message = message
        self.recommendation = recommendation
    
    def __str__(self):
        icon = "❌" if self.severity == "ERROR" else "⚠️" if self.severity == "WARNING" else "ℹ️"
        msg = f"{icon} [{self.component}] {self.message}"
        if self.recommendation:
            msg += f"\n💡 Recommendation: {self.recommendation}"
        return msg


def validate_metadata(metadata_file="pachyderm_metadata.json"):
    """
    Validate metadata against schema with strict enforcement.
    
    Args:
        metadata_file: Path to metadata JSON file
        
    Returns:
        Tuple of (is_valid, alerts_list)
    """
    alerts = []
    
    # Load metadata
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
    except FileNotFoundError:
        alerts.append(ValidationAlert(
            "ERROR", "FILE", "metadata", 
            f"Metadata file '{metadata_file}' not found",
            "Ensure the BOD generator has been run first"
        ))
        return False, alerts
    except json.JSONDecodeError as e:
        alerts.append(ValidationAlert(
            "ERROR", "FILE", "metadata",
            f"Invalid JSON format: {e}",
            "Check JSON syntax in metadata file"
        ))
        return False, alerts
    
    # Schema validation
    try:
        jsonschema.validate(instance=metadata, schema=PACHYDERM_SCHEMA)
    except jsonschema.ValidationError as e:
        path = " -> ".join(str(p) for p in e.path) if e.path else "root"
        alerts.append(ValidationAlert(
            "ERROR", path, e.validator,
            f"Schema validation failed: {e.message}",
            "Correct the metadata structure to match schema requirements"
        ))
        return False, alerts
    
    # Additional business logic validations
    
    # Check generator ratings
    for gen in metadata.get("generators", []):
        kw = gen.get("kw", 0)
        kva = gen.get("kva", 0)
        if kva < kw:
            alerts.append(ValidationAlert(
                "WARNING", gen["id"], "kva",
                f"kVA ({kva}) should be >= kW ({kw})",
                "Verify generator power factor and ratings"
            ))
    
    # Check UPS battery compatibility
    for ups in metadata.get("ups", []):
        if ups.get("type") == "ROTARY" and ups.get("battery") not in ["FLYWHEEL", "NICD"]:
            alerts.append(ValidationAlert(
                "WARNING", ups["id"], "battery",
                f"Rotary UPS with {ups.get('battery')} battery is uncommon",
                "Rotary UPS typically use flywheel energy storage"
            ))
        
        if ups.get("function") == "IT" and ups.get("type") == "ROTARY":
            alerts.append(ValidationAlert(
                "INFO", ups["id"], "type",
                "Rotary UPS for IT loads requires careful synchronization",
                "Consider static UPS with Li-ion for IT critical loads per TIA-942-A"
            ))
    
    # Check earthing transformer impedance ratios
    for earth in metadata.get("earthing_tx", []):
        imp = earth.get("impedance", {})
        r = imp.get("r_ohm", 0)
        x = imp.get("x_ohm", 0)
        if x > 0:
            ratio = r / x
            if ratio < 4 or ratio > 6:
                alerts.append(ValidationAlert(
                    "WARNING", earth["id"], "impedance",
                    f"R/X ratio ({ratio:.2f}) outside typical range (4-6)",
                    "Verify earthing impedance for optimal fault current limitation"
                ))
    
    # Check MV/LV switchboard ratings
    for swbd in metadata.get("mv_swbd", []) + metadata.get("lv_swbd", []):
        if "redundancy" not in swbd:
            alerts.append(ValidationAlert(
                "WARNING", swbd["id"], "redundancy",
                "Missing redundancy field",
                "Define redundancy as 'A', 'B', 'A/B', or 'N+1' based on Tier requirements"
            ))
    
    # Check topology-specific requirements
    topology = metadata.get("topology", "radial")
    if topology == "ring":
        rmu_count = len(metadata.get("rmu", []))
        if rmu_count < 4:
            alerts.append(ValidationAlert(
                "WARNING", "RMU", "count",
                f"Ring bus has only {rmu_count} RMUs (expected 4)",
                "Ensure proper ring segmentation with RMUs at each node"
            ))
    
    if topology == "dual":
        mv_count = len(metadata.get("mv_swbd", []))
        if mv_count < 2:
            alerts.append(ValidationAlert(
                "WARNING", "MV_SWBD", "count",
                f"Dual-feed system has only {mv_count} MV switchboards (expected 2)",
                "Dual-feed requires separate A and B switchboards for redundancy"
            ))
    
    if topology == "distributed_redundant":
        mv_count = len(metadata.get("mv_swbd", []))
        if mv_count < 2:
            alerts.append(ValidationAlert(
                "WARNING", "MV_SWBD", "count",
                f"Distributed redundant (2N) system has only {mv_count} MV switchboards (expected 2)",
                "2N architecture requires completely independent A and B power trains"
            ))
        
        # Check for tie breakers (shouldn't exist in true 2N)
        tie_breakers = [s for s in metadata.get("switches", []) if "TIE" in s.get("id", "").upper()]
        if tie_breakers:
            alerts.append(ValidationAlert(
                "WARNING", "BUS_TIE", "topology",
                "Tie breaker detected in distributed redundant (2N) topology",
                "True 2N systems have completely isolated A and B paths with no tie breakers"
            ))
        
        # Verify 2N redundancy classification
        for swbd in metadata.get("mv_swbd", []) + metadata.get("lv_swbd", []):
            if swbd.get("redundancy") not in ["2N", "A", "B"]:
                alerts.append(ValidationAlert(
                    "INFO", swbd["id"], "redundancy",
                    f"Switchboard redundancy '{swbd.get('redundancy')}' in 2N system",
                    "Distributed redundant systems typically use '2N' redundancy classification"
                ))
    
    # Check if z_matrix exists for earthing transformers
    if metadata.get("include_z_matrix"):
        for earth in metadata.get("earthing_tx", []):
            if "z_matrix_3ph" not in earth or not earth["z_matrix_3ph"]:
                alerts.append(ValidationAlert(
                    "INFO", earth["id"], "z_matrix_3ph",
                    "3-phase Z-matrix not included",
                    "Enable 3-phase impedance matrix for comprehensive fault analysis"
                ))
    
    is_valid = all(alert.severity != "ERROR" for alert in alerts)
    return is_valid, alerts


def generate_validation_report(alerts, output_file="validation_report.txt"):
    """
    Generate human-readable validation report.
    
    Args:
        alerts: List of ValidationAlert objects
        output_file: Path to output report file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    error_count = sum(1 for a in alerts if a.severity == "ERROR")
    warning_count = sum(1 for a in alerts if a.severity == "WARNING")
    info_count = sum(1 for a in alerts if a.severity == "INFO")
    
    # Build report
    report_lines = [
        "=" * 70,
        "PACHYDERM GLOBAL - Electrical Model Validation Report",
        "=" * 70,
        f"Timestamp: {timestamp}",
        f"Validator Version: 1.0.0",
        "",
        "-" * 70,
        "Validation Summary",
        "-" * 70,
        f"❌ {error_count} Error(s)",
        f"⚠️  {warning_count} Warning(s)",
        f"ℹ️  {info_count} Info Message(s)",
        "",
        "-" * 70,
        "Alerts and Recommendations",
        "-" * 70,
    ]
    
    if not alerts:
        report_lines.append("✅ No issues found - validation passed successfully!")
    else:
        for alert in alerts:
            report_lines.append("")
            report_lines.append(str(alert))
    
    report_lines.extend([
        "",
        "-" * 70,
        "Result",
        "-" * 70,
        f"Validation Status: {'FAILED' if error_count > 0 else 'PASSED WITH WARNINGS' if warning_count > 0 else 'PASSED'}",
        "-" * 70,
        "",
        "References:",
        "- IEEE Std 1100 (Emerald Book): Powering and Grounding Electronic Equipment",
        "- IEEE Std 142 (Green Book): Grounding of Industrial and Commercial Power Systems",
        "- TIA-942-A: Telecommunications Infrastructure Standard for Data Centers",
        "- IEC 60909: Short-circuit currents in three-phase a.c. systems",
        "=" * 70
    ])
    
    report_content = "\n".join(report_lines)
    
    # Write to file
    with open(output_file, 'w') as f:
        f.write(report_content)
    
    return report_content


def main():
    """Run validation and display results."""
    print("=" * 70)
    print("PACHYDERM GLOBAL - Metadata Validator")
    print("=" * 70)
    print("\nValidating pachyderm_metadata.json...")
    
    is_valid, alerts = validate_metadata()
    
    # Display alerts
    if alerts:
        print(f"\nFound {len(alerts)} alert(s):\n")
        for alert in alerts:
            print(alert)
            print()
    else:
        print("\n✅ No issues found - validation passed successfully!")
    
    # Generate report
    report_content = generate_validation_report(alerts)
    print("\n✅ Validation report saved: validation_report.txt")
    
    # Summary
    print("\n" + "=" * 70)
    if is_valid:
        print("Validation Status: PASSED" + (" WITH WARNINGS" if alerts else ""))
    else:
        print("Validation Status: FAILED")
    print("=" * 70)


if __name__ == "__main__":
    main()
