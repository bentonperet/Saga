#!/usr/bin/env python3
"""
Batch download script for Siemens Single-Line Electrical Symbols
Downloads SVG symbols from symbols.radicasoftware.com
"""

import requests
import os
import time
from pathlib import Path

# Base URL pattern for symbol downloads
BASE_URL = "https://symbols-electrical.getvecta.com/stencil_229/"

# Symbol definitions: (ID, filename, description)
SYMBOLS = [
    # Contactors and Circuit Breakers
    (0, "contactor-3p", "Contactor 3P"),
    (1, "circuit-breaker-3p", "Circuit Breaker 3P"),
    (2, "disconnector-isolator-3p", "Disconnector/Isolator 3P"),
    (3, "switch-disconnector-3p", "Switch Disconnector 3P"),
    (4, "fuse-disconnector-isolator-3p", "Fuse Disconnector/Isolator 3P"),
    (5, "fuse-switch-disconnector-3p", "Fuse Switch Disconnector 3P"),
    (9, "fuse-3p", "Fuse 3P"),

    # Switches
    (6, "selector-switch-1p", "Selector Switch 1P"),
    (7, "selector-switch-2p", "Selector Switch 2P"),
    (8, "selector-switch-3p", "Selector Switch 3P"),
    (17, "manual-switch", "Manual Switch"),
    (18, "emergency-stop-switch", "Emergency Stop Switch"),
    (22, "key-selector-switch", "Key Selector Switch"),

    # Contacts
    (12, "normally-open-contact", "Normally Open Contact"),
    (13, "normally-close-contact", "Normally Close Contact"),
    (14, "changeover-contact-break-before-make", "ChangeOver Contact"),

    # Circuit Breakers (various types)
    (36, "circuit-breaker-thermal-magnetic-3p", "Circuit Breaker Thermal & Magnetic 3P"),
    (37, "circuit-breaker-thermal-3p", "Circuit Breaker Thermal 3P"),
    (38, "circuit-breaker-magnetic-3p", "Circuit Breaker Magnetic 3P"),

    # Relays
    (44, "under-voltage-relay", "Undervoltage Relay"),
    (45, "earth-fault-relay", "Earth Fault Relay"),
    (46, "instantaneous-overcurrent-relay", "Instantaneous OverCurrent Relay"),
    (51, "thermal-overload-relay", "Thermal Overload Relay"),

    # Transformers
    (57, "transformer-3p", "Transformer 3P"),
    (59, "autotransformer-3p", "AutoTransformer 3P"),
    (60, "current-transformer", "Current Transformer"),
    (61, "voltage-transformer", "Voltage Transformer"),
    (63, "transformer-3p-star-delta", "Transformer 3P Star-Delta"),

    # Motors
    (66, "motor-3p", "Motor 3P"),
    (67, "motor-3p-star", "Motor 3P Star"),
    (68, "motor-3p-delta", "Motor 3P Delta"),

    # Generators and Power Sources
    (75, "generator", "Generator"),
    (76, "battery", "Battery"),
    (77, "power-supply-converter-dc-dc", "Power Supply DC/DC Converter"),

    # Measurement Devices
    (78, "ammeter", "Ammeter"),
    (79, "voltmeter", "Voltmeter"),
    (80, "wattmeter", "Wattmeter"),
    (81, "frequency-meter", "Frequency Meter"),
    (82, "power-factor-meter", "Power Factor Meter"),

    # Indicators
    (10, "pilot-light", "Pilot Light"),
    (11, "photo-cell", "Photo Cell"),

    # Grounding
    (117, "earth-ground", "Earth/Ground"),

    # Busbars
    (118, "busbar-3p", "Busbar 3P"),

    # UPS and Power Systems
    (120, "ups", "UPS (Uninterruptible Power Supply)"),
]

def download_symbol(symbol_id, filename, description, output_dir):
    """
    Download a single symbol from the Siemens library

    Args:
        symbol_id: Numeric ID of the symbol
        filename: Base filename (e.g., 'transformer-3p')
        description: Human-readable description
        output_dir: Directory to save the symbol
    """
    # Construct the download URL
    # Pattern: https://symbols-electrical.getvecta.com/stencil_229/{id}_{filename}.{hash}.svg
    # We'll try the common pattern first
    url = f"{BASE_URL}{symbol_id}_{filename}.svg"

    output_path = output_dir / f"{symbol_id:03d}_{filename}.svg"

    try:
        print(f"Downloading {description} (ID: {symbol_id})...", end=" ")
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"[OK] Success ({len(response.content)} bytes)")
            return True
        else:
            print(f"[FAIL] HTTP {response.status_code}")
            return False

    except Exception as e:
        print(f"[ERROR] {e}")
        return False

def main():
    """Main download function"""
    # Create output directory
    output_dir = Path("siemens_symbols")
    output_dir.mkdir(exist_ok=True)

    print("=" * 70)
    print("SIEMENS SINGLE-LINE ELECTRICAL SYMBOLS BATCH DOWNLOADER")
    print("=" * 70)
    print(f"Output directory: {output_dir.absolute()}")
    print(f"Total symbols to download: {len(SYMBOLS)}")
    print("=" * 70)
    print()

    successful = 0
    failed = 0

    for symbol_id, filename, description in SYMBOLS:
        if download_symbol(symbol_id, filename, description, output_dir):
            successful += 1
        else:
            failed += 1

        # Be polite to the server
        time.sleep(0.5)

    print()
    print("=" * 70)
    print("DOWNLOAD SUMMARY")
    print("=" * 70)
    print(f"Successful downloads: {successful}")
    print(f"Failed downloads: {failed}")
    print(f"Total symbols: {len(SYMBOLS)}")
    print(f"Success rate: {(successful/len(SYMBOLS)*100):.1f}%")
    print("=" * 70)
    print()
    print(f"Symbols saved to: {output_dir.absolute()}")

    # Create a catalog file
    catalog_path = output_dir / "CATALOG.txt"
    with open(catalog_path, 'w') as f:
        f.write("SIEMENS SINGLE-LINE ELECTRICAL SYMBOLS CATALOG\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Downloaded: {successful}/{len(SYMBOLS)} symbols\n")
        f.write(f"Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("SYMBOL LIST:\n")
        f.write("-" * 70 + "\n")
        for symbol_id, filename, description in SYMBOLS:
            f.write(f"{symbol_id:3d}  {filename:45s}  {description}\n")

    print(f"Catalog saved to: {catalog_path}")

if __name__ == "__main__":
    main()
