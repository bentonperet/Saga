"""
Debug script to test regex patterns against actual BOD
"""
import re
from pathlib import Path

# Read BOD
bod_file = Path(r"C:\Users\eriks\Documents\Obsidian\Saga Pryor DC\Basis of Design\7BOD - Electrical (CSI Div 26).md")
with open(bod_file, 'r', encoding='utf-8') as f:
    text = f.read()

print("=" * 80)
print("DEBUGGING REGEX PATTERNS")
print("=" * 80)

# Test 1: Generator count
print("\n1. TESTING GENERATOR COUNT PATTERNS")
print("-" * 80)
gen_section = re.search(r'##\s*GENERATOR SYSTEM.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
if gen_section:
    search_text = gen_section.group(0)
    print(f"Generator section found ({len(search_text)} chars)")
    print(f"First 200 chars: {search_text[:200]}")

    patterns = [
        r'\*\*(\d+)\s*[×x]\s*[\d.]+\s*(?:MW|kW|kVA).*?[Gg]enerator',
        r'(\d+)\s*[×x]\s*[\d.]+\s*(?:MW|kW|kVA).*?[Gg]enerator',
    ]

    for i, pattern in enumerate(patterns):
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            print(f"Pattern {i+1} MATCHED: {match.group(0)}")
            print(f"  Captured count: {match.group(1)}")
        else:
            print(f"Pattern {i+1} NO MATCH")
else:
    print("Generator section NOT FOUND")

# Test 2: Generator rating
print("\n2. TESTING GENERATOR RATING PATTERNS")
print("-" * 80)
if gen_section:
    search_text = gen_section.group(0)

    patterns = [
        r'\*\*(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)\s*@',
        r'(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)\s*@',
        r'[×x]\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)',
    ]

    for i, pattern in enumerate(patterns):
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            print(f"Pattern {i+1} MATCHED: {match.group(0)}")
            print(f"  Captured value: {match.group(1)} {match.group(2)}")
        else:
            print(f"Pattern {i+1} NO MATCH")

# Test 3: IT UPS
print("\n3. TESTING IT UPS PATTERNS")
print("-" * 80)
it_ups_section = re.search(r'##\s*IT UPS.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
if it_ups_section:
    section = it_ups_section.group(0)
    print(f"IT UPS section found ({len(section)} chars)")

    # Find Phase 1 heading
    phase1_match = re.search(r'###\s*Phase 1:.*', section, re.IGNORECASE)
    if phase1_match:
        print(f"Phase 1 heading: {phase1_match.group(0)}")

    patterns = [
        r'\*\*Phase 1:\*\*\s*(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA',
        r'###\s*Phase 1:\s*(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA',  # Heading format
        r'(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA.*?(?:UPS\s+Module|module)',
    ]

    for i, pattern in enumerate(patterns):
        match = re.search(pattern, section, re.IGNORECASE)
        if match:
            print(f"Pattern {i+1} MATCHED: {match.group(0)[:80]}")
            print(f"  Count: {match.group(1)}, Rating: {match.group(2)} kVA")
        else:
            print(f"Pattern {i+1} NO MATCH")
else:
    print("IT UPS section NOT FOUND")

# Test 4: Mechanical UPS
print("\n4. TESTING MECHANICAL UPS PATTERNS")
print("-" * 80)
mech_ups_section = re.search(r'##\s*MECHANICAL UPS.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
if mech_ups_section:
    section = mech_ups_section.group(0)
    print(f"Mechanical UPS section found ({len(section)} chars)")

    # Find Phase 1 line
    phase1_match = re.search(r'\*\*Phase 1:.*', section, re.IGNORECASE)
    if phase1_match:
        print(f"Phase 1 line: {phase1_match.group(0)}")

    patterns = [
        r'\*\*Phase 1:\*\*\s*(\d+)\s*[×x]\s*([\d,]+)\s*kW',
        r'(\d+)\s*[×x]\s*([\d,]+)\s*kW.*?(?:UPS\s+Module|module)',
    ]

    for i, pattern in enumerate(patterns):
        match = re.search(pattern, section, re.IGNORECASE)
        if match:
            print(f"Pattern {i+1} MATCHED: {match.group(0)[:80]}")
            print(f"  Count: {match.group(1)}, Rating: {match.group(2)} kW")
        else:
            print(f"Pattern {i+1} NO MATCH")
else:
    print("Mechanical UPS section NOT FOUND")
