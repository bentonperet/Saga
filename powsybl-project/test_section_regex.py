"""Test section extraction regex"""
import re
from pathlib import Path

bod_file = Path(r"C:\Users\eriks\Documents\Obsidian\Saga Pryor DC\Basis of Design\7BOD - Electrical (CSI Div 26).md")
with open(bod_file, 'r', encoding='utf-8') as f:
    text = f.read()

print(f"Total BOD length: {len(text)} chars\n")

# Test 1: Current pattern
print("TEST 1: Current pattern with re.DOTALL")
pattern1 = r'##\s*GENERATOR SYSTEM.*?(?=##|\Z)'
match1 = re.search(pattern1, text, re.DOTALL | re.IGNORECASE)
if match1:
    section = match1.group(0)
    print(f"  Match length: {len(section)} chars")
    print(f"  First 100 chars: {section[:100]}")
    print(f"  Last 100 chars: {section[-100:]}")
else:
    print("  NO MATCH")

# Test 2: Try with \n\n## as delimiter
print("\nTEST 2: Pattern with newline before next ##")
pattern2 = r'##\s*GENERATOR SYSTEM.*?(?=\n##|\Z)'
match2 = re.search(pattern2, text, re.DOTALL | re.IGNORECASE)
if match2:
    section = match2.group(0)
    print(f"  Match length: {len(section)} chars")
    print(f"  Contains '6 × 4.0 MW': {'6 × 4.0 MW' in section}")
    print(f"  Contains 'Diesel Generators': {'Diesel Generators' in section}")
else:
    print("  NO MATCH")

# Test 3: Manual extraction
print("\nTEST 3: Find line numbers")
lines = text.split('\n')
gen_start = None
gen_end = None
for i, line in enumerate(lines):
    if line.strip().startswith('## GENERATOR SYSTEM'):
        gen_start = i
        print(f"  Generator section starts at line {i}: {line}")
    elif gen_start and line.strip().startswith('## ') and 'GENERATOR' not in line:
        gen_end = i
        print(f"  Next section starts at line {i}: {line}")
        break

if gen_start and gen_end:
    manual_section = '\n'.join(lines[gen_start:gen_end])
    print(f"  Manual extraction length: {len(manual_section)} chars")
    print(f"  Contains '6 × 4.0 MW': {'6 × 4.0 MW' in manual_section}")
    print(f"  Contains '**6 × 4.0 MW': {'**6 × 4.0 MW' in manual_section}")

# Test 4: Search for the specific text
print("\nTEST 4: Direct search for generator spec")
spec_match = re.search(r'6\s*×\s*4\.0\s*MW', text)
if spec_match:
    print(f"  FOUND spec at position {spec_match.start()}")
    print(f"  Context: {text[spec_match.start()-20:spec_match.end()+40]}")
else:
    print("  NOT FOUND")
