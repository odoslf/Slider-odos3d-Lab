#!/usr/bin/env python3
from pathlib import Path
import re
import sys

failed = False


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def fail(msg: str) -> None:
    global failed
    print(f"FAIL: {msg}")
    failed = True


def must_exist(path: str) -> Path:
    p = Path(path)
    if not p.is_file():
        fail(f"{path} does not exist")
        return p
    ok(f"{path} exists")
    return p


checks = [
    ("docs/privacy-policy.md", ["Smart Timelapse AI"]),
    ("docs/terms.md", ["Smart Timelapse AI"]),
    ("docs/index.md", ["Slider-odos3d", "Smart Timelapse AI"]),
]

for rel, needles in checks:
    p = must_exist(rel)
    if not p.is_file():
        continue
    content = p.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in content:
            fail(f"'{needle}' not found in {rel}")
        else:
            ok(f"'{needle}' found in {rel}")

for required_file in [
    "docs/downloads.md",
    "docs/gallery.md",
    "docs/parts.md",
    "docs/parts/_TEMPLATE_PART.md",
]:
    must_exist(required_file)

topnav_path = must_exist("docs/_includes/topnav.html")
if topnav_path.is_file():
    topnav = topnav_path.read_text(encoding="utf-8")
    for route in ["/downloads/", "/gallery/", "/parts/"]:
        if f"'{route}'" not in topnav and f'"{route}"' not in topnav:
            fail(f"{route} link not found in docs/_includes/topnav.html")
        else:
            ok(f"{route} link found in docs/_includes/topnav.html")

privacy_path = must_exist("docs/privacy-policy.md")
privacy = privacy_path.read_text(encoding="utf-8") if privacy_path.is_file() else ""

for banned in [
    "aplica a la app **Slider-odos3d",
    "Slider-odos3d está diseñada",
]:
    if banned in privacy:
        fail(f"banned phrase '{banned}' found in docs/privacy-policy.md")
    else:
        ok(f"banned phrase '{banned}' not found in docs/privacy-policy.md")

for required in ["publicidad", "pago único", "Smart Timelapse AI"]:
    if required not in privacy:
        fail(f"'{required}' not found in docs/privacy-policy.md")
    else:
        ok(f"'{required}' found in docs/privacy-policy.md")

# LAB 5 hardening
for rel in ["docs/privacy-policy.md", "docs/terms.md"]:
    p = must_exist(rel)
    if not p.is_file():
        continue
    content = p.read_text(encoding="utf-8")
    if re.search(r"\bO2\b", content):
        fail(f"'O2' found in {rel}")
    else:
        ok(f"'O2' not found in {rel}")

if privacy:
    for required in [
        "Responsable: Javier López Flores",
        "ODOS3D (odoslf)",
        "odos3d@gmail.com",
    ]:
        if required not in privacy:
            fail(f"'{required}' not found in docs/privacy-policy.md")
        else:
            ok(f"'{required}' found in docs/privacy-policy.md")

support_path = must_exist("docs/support.md")
if support_path.is_file():
    support = support_path.read_text(encoding="utf-8")
    h3_count = len(re.findall(r"^###\s+", support, flags=re.M))
    faq_list_count = len(re.findall(r"^\s*[-*]\s+", support, flags=re.M))
    if h3_count >= 8 or faq_list_count >= 8:
        ok("docs/support.md contains at least 8 FAQ entries")
    else:
        fail("docs/support.md must contain at least 8 FAQ entries (### headings or list items)")

downloads_path = must_exist("docs/downloads.md")
if downloads_path.is_file():
    downloads = downloads_path.read_text(encoding="utf-8")
    if ".gitkeep" in downloads or "en preparación" in downloads:
        ok("docs/downloads.md includes hardware status notice (.gitkeep/en preparación)")
    else:
        fail("docs/downloads.md must include '.gitkeep' or 'en preparación'")

config_path = must_exist("docs/_config.yml")
if config_path.is_file():
    for line in config_path.read_text(encoding="utf-8").splitlines():
        lower_line = line.lower()
        if lower_line.startswith("description:") and "legal" in lower_line and "para" in lower_line and "slider-odos3d" in lower_line:
            fail("docs/_config.yml description must not say legal para Slider-odos3d")
            break
    else:
        ok("docs/_config.yml description does not say legal para Slider-odos3d")

if failed:
    sys.exit(1)

print("All branding/download/gallery/parts checks passed.")
