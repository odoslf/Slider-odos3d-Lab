#!/usr/bin/env python3
from pathlib import Path
import sys

checks = [
    ("docs/privacy-policy.md", ["Smart Timelapse AI"]),
    ("docs/terms.md", ["Smart Timelapse AI"]),
    ("docs/index.md", ["Slider-odos3d", "Smart Timelapse AI"]),
]

failed = False
for rel, needles in checks:
    content = Path(rel).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in content:
            print(f"FAIL: '{needle}' not found in {rel}")
            failed = True
        else:
            print(f"OK: '{needle}' found in {rel}")

# Guardrail LAB 2 + LAB 3
for required_file in [
    "docs/downloads.md",
    "docs/gallery.md",
    "docs/parts.md",
    "docs/parts/_TEMPLATE_PART.md",
]:
    if not Path(required_file).is_file():
        print(f"FAIL: {required_file} does not exist")
        failed = True
    else:
        print(f"OK: {required_file} exists")

topnav = Path("docs/_includes/topnav.html").read_text(encoding="utf-8")
for route in ["/downloads/", "/gallery/", "/parts/"]:
    if f"'{route}'" not in topnav and f'"{route}"' not in topnav:
        print(f"FAIL: {route} link not found in docs/_includes/topnav.html")
        failed = True
    else:
        print(f"OK: {route} link found in docs/_includes/topnav.html")


privacy = Path("docs/privacy-policy.md").read_text(encoding="utf-8")

for banned in [
    "aplica a la app **Slider-odos3d",
    "Slider-odos3d está diseñada",
]:
    if banned in privacy:
        print(f"FAIL: banned phrase '{banned}' found in docs/privacy-policy.md")
        failed = True
    else:
        print(f"OK: banned phrase '{banned}' not found in docs/privacy-policy.md")

for required in ["publicidad", "pago único", "Smart Timelapse AI"]:
    if required not in privacy:
        print(f"FAIL: '{required}' not found in docs/privacy-policy.md")
        failed = True
    else:
        print(f"OK: '{required}' found in docs/privacy-policy.md")

config = Path("docs/_config.yml").read_text(encoding="utf-8").lower()
for line in Path("docs/_config.yml").read_text(encoding="utf-8").splitlines():
    lower_line = line.lower()
    if lower_line.startswith("description:") and "legal" in lower_line and "para" in lower_line and "slider-odos3d" in lower_line:
        print("FAIL: docs/_config.yml description must not say legal para Slider-odos3d")
        failed = True
        break
else:
    print("OK: docs/_config.yml description does not say legal para Slider-odos3d")

if failed:
    sys.exit(1)

print("All branding/download/gallery/parts checks passed.")
