#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


PUBLIC_PAGES = {
    "/": "docs/index.html",
    "/hardware/": "docs/index.md",
    "/downloads/": "docs/downloads.md",
    "/support/": "docs/support.md",
    "/gallery/": "docs/gallery.md",
    "/privacy-policy/": "docs/privacy-policy.md",
    "/terms/": "docs/terms.md",
    "/grbl/": "docs/grbl.md",
    "/troubleshooting/": "docs/troubleshooting.md",
    "/app-screens/": "docs/app-screens.md",
    "/quick-assembly/": "docs/quick_assembly.md",
    "/assembly-guide/": "docs/assembly_guide.md",
    "/calibration/": "docs/calibration.md",
    "/en/": "docs/en/index.html",
    "/en/hardware/": "docs/en/hardware.md",
    "/en/downloads/": "docs/en/downloads.md",
    "/en/support/": "docs/en/support.md",
    "/en/gallery/": "docs/en/gallery.md",
    "/en/privacy-policy/": "docs/en/privacy-policy.md",
    "/en/terms/": "docs/en/terms.md",
    "/en/grbl/": "docs/en/grbl.md",
    "/en/troubleshooting/": "docs/en/troubleshooting.md",
    "/en/app-screens/": "docs/en/app-screens.md",
    "/en/quick-assembly/": "docs/en/quick-assembly.md",
    "/en/assembly-guide/": "docs/en/assembly-guide.md",
    "/en/calibration/": "docs/en/calibration.md",
}

REDIRECT_PAGES = {
    "/privacy-app/": "docs/privacy-app.md",
    "/photo-guidelines/": "docs/photo_guidelines.md",
    "/publish-checklist/": "docs/publish_checklist.md",
    "/release-checklist-v1/": "docs/release_checklist_v1.md",
    "/upload-map/": "docs/upload_map.md",
    "/pages-setup/": "docs/README_PAGES.md",
    "/upload-workflow/": "docs/UPLOAD_WORKFLOW.md",
    "/parts/": "docs/parts.md",
}

STL_NAMES = [
    "slider-odos3d-lab-caja-electronica-v1.stl",
    "slider-odos3d-lab-carro-v1.stl",
    "slider-odos3d-lab-escuadra-v1.stl",
    "slider-odos3d-lab-separador-v1.stl",
    "slider-odos3d-lab-soporte-correa-v1.stl",
    "slider-odos3d-lab-soporte-derecho-v1.stl",
    "slider-odos3d-lab-soporte-izquierdo-v1.stl",
    "slider-odos3d-lab-tapa-electronica-v1.stl",
    "slider-odos3d-lab-tubo-camara-v1.stl",
]

FORBIDDEN_PUBLIC_ROUTES_IN_SITEMAP = [
    "/privacy-app/",
    "/photo-guidelines/",
    "/publish-checklist/",
    "/release-checklist-v1/",
    "/upload-map/",
    "/pages-setup/",
    "/upload-workflow/",
    "/parts/",
    "/smart-timelapse-ai/",
    "/en/smart-timelapse-ai/",
]

TEXT_EXTENSIONS = {
    ".md",
    ".html",
    ".yml",
    ".yaml",
    ".xml",
    ".txt",
    ".webmanifest",
    ".css",
    ".scss",
    ".js",
    ".json",
    ".py",
}


class Audit:
    def __init__(self) -> None:
        self.errors: dict[str, list[str]] = {}

    def fail(self, category: str, message: str) -> None:
        self.errors.setdefault(category, []).append(message)

    def require(self, category: str, condition: bool, message: str) -> None:
        if not condition:
            self.fail(category, message)

    def summary(self) -> int:
        print("\n=== Public Site Audit Summary ===")
        if not self.errors:
            print("PASS")
            return 0

        total = sum(len(items) for items in self.errors.values())
        for category in sorted(self.errors):
            print(f"\n[{category}] {len(self.errors[category])} issue(s)")
            for item in self.errors[category]:
                print(f" - {item}")

        print(f"\nFAIL ({total} issue(s))")
        return 1


def path(rel: str) -> Path:
    return ROOT / rel


def read(rel: str) -> str:
    return path(rel).read_text(encoding="utf-8")


def text_files() -> list[Path]:
    result: list[Path] = []
    for base in [ROOT / "docs", ROOT / "scripts", ROOT]:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and p.suffix in TEXT_EXTENSIONS:
                if ".git" not in p.parts:
                    result.append(p)
    return sorted(set(result))


def parse_front_matter(rel: str) -> dict[str, str]:
    txt = read(rel)
    lines = txt.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break

    if end is None:
        return {}

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def collect_permalinks() -> dict[str, list[str]]:
    routes: dict[str, list[str]] = {}
    for p in (ROOT / "docs").rglob("*"):
        if not p.is_file() or p.suffix not in {".md", ".html"}:
            continue
        rel = p.relative_to(ROOT).as_posix()
        fm = parse_front_matter(rel)
        permalink = fm.get("permalink")
        if permalink:
            routes.setdefault(permalink, []).append(rel)
    return routes


def validate_files_exist(audit: Audit) -> None:
    required = [
        "docs/_config.yml",
        "docs/_data/public-links.yml",
        "docs/_data/public-media.yml",
        "docs/_data/gallery-media.yml",
        "docs/_data/asset-status.yml",
        "docs/_includes/head-custom.html",
        "docs/_includes/public-site-header.html",
        "docs/_includes/public-site-footer.html",
        "docs/_includes/gallery-media-item.html",
        "docs/_layouts/public-page.html",
        "docs/site.webmanifest",
        "docs/sitemap.xml",
        "docs/robots.txt",
        "docs/404.html",
    ]

    for rel in required:
        audit.require("FILES", path(rel).exists(), f"Missing required file: {rel}")

    for rel in PUBLIC_PAGES.values():
        audit.require("FILES", path(rel).exists(), f"Missing public page source: {rel}")

    for rel in REDIRECT_PAGES.values():
        audit.require("FILES", path(rel).exists(), f"Missing redirect page source: {rel}")

    for name in STL_NAMES:
        audit.require("STL_FILES", path(f"prints/STL/v1/{name}").exists(), f"Missing STL: {name}")


def validate_routes(audit: Audit) -> None:
    routes = collect_permalinks()

    for route, rel in PUBLIC_PAGES.items():
        audit.require("ROUTES", route in routes, f"Missing permalink route: {route}")
        if route in routes:
            audit.require("ROUTES", rel in routes[route], f"Route {route} should map to {rel}, found {routes[route]}")
            audit.require("ROUTES", len(routes[route]) == 1, f"Route {route} has duplicate sources: {routes[route]}")

    for route, rel in REDIRECT_PAGES.items():
        audit.require("REDIRECTS", route in routes, f"Missing redirect route: {route}")
        if route in routes:
            audit.require("REDIRECTS", rel in routes[route], f"Redirect {route} should map to {rel}, found {routes[route]}")
            audit.require("REDIRECTS", len(routes[route]) == 1, f"Redirect {route} has duplicate sources: {routes[route]}")


def validate_public_pages(audit: Audit) -> None:
    for route, rel in PUBLIC_PAGES.items():
        txt = read(rel)
        fm = parse_front_matter(rel)

        if route in {"/", "/en/"}:
            audit.require("PUBLIC_PAGES", "<title>" in txt, f"{rel} must define title")
            audit.require("PUBLIC_PAGES", "meta name=\"description\"" in txt, f"{rel} must define description")
            continue

        audit.require("PUBLIC_PAGES", fm.get("layout") == "public-page", f"{rel} must use layout: public-page")
        audit.require("PUBLIC_PAGES", fm.get("permalink") == route, f"{rel} must use permalink {route}")
        audit.require("PUBLIC_PAGES", bool(fm.get("title")), f"{rel} missing title")
        audit.require("PUBLIC_PAGES", bool(fm.get("description")), f"{rel} missing description")
        audit.require("PUBLIC_PAGES", bool(fm.get("lang")), f"{rel} missing lang")
        audit.require("PUBLIC_PAGES", bool(fm.get("lang_page")), f"{rel} missing lang_page")

        if route.startswith("/en/"):
            audit.require("PUBLIC_PAGES", fm.get("lang_page") == "en", f"{rel} must have lang_page: en")
        else:
            audit.require("PUBLIC_PAGES", fm.get("lang_page") == "es", f"{rel} must have lang_page: es")


def validate_redirects(audit: Audit) -> None:
    for route, rel in REDIRECT_PAGES.items():
        txt = read(rel)
        fm = parse_front_matter(rel)

        audit.require("REDIRECTS", fm.get("layout") == "null", f"{rel} must use layout: null")
        audit.require("REDIRECTS", fm.get("permalink") == route, f"{rel} must use permalink {route}")
        audit.require("REDIRECTS", fm.get("sitemap") == "false", f"{rel} must use sitemap: false")
        audit.require("REDIRECTS", "noindex,follow" in txt, f"{rel} must include robots noindex,follow")
        audit.require("REDIRECTS", "http-equiv=\"refresh\"" in txt, f"{rel} must include meta refresh")
        audit.require("REDIRECTS", "rel=\"canonical\"" in txt, f"{rel} must include canonical")


def validate_public_links(audit: Audit) -> None:
    txt = read("docs/_data/public-links.yml")

    required = [
        "support_email: \"odos3d.Lab@gmail.com\"",
        "legal_responsible_name: \"Silvia Díaz Celaya\"",
        "grbl: \"/grbl/\"",
        "troubleshooting: \"/troubleshooting/\"",
        "grbl: \"/en/grbl/\"",
        "troubleshooting: \"/en/troubleshooting/\"",
    ]

    for token in required:
        audit.require("PUBLIC_LINKS", token in txt, f"public-links missing: {token}")


def validate_public_media(audit: Audit) -> None:
    txt = read("docs/_data/public-media.yml")

    audit.require("PUBLIC_MEDIA", "final_path: \"/assets/media/app/logo-final.png\"" in txt, "favicon/logo must use logo-final.png")
    audit.require("PUBLIC_MEDIA", "final_path: \"/assets/media/app/hero-final.jpg\"" in txt, "hero/og must use hero-final.jpg")
    audit.require("PUBLIC_MEDIA", "favicon_32:" not in txt, "public-media must not define favicon_32")
    audit.require("PUBLIC_MEDIA", "favicon_16:" not in txt, "public-media must not define favicon_16")
    audit.require("PUBLIC_MEDIA", "apple_touch_icon:" not in txt, "public-media must not define apple_touch_icon")

    favicon_block = re.search(r"\n  favicon:\n(?P<body>(?:    .+\n)+)", txt)
    audit.require("PUBLIC_MEDIA", favicon_block is not None, "public-media missing favicon block")
    if favicon_block:
        body = favicon_block.group("body")
        audit.require("PUBLIC_MEDIA", "final_path: \"/assets/media/app/logo-final.png\"" in body, "favicon block must point to logo-final.png")
        audit.require("PUBLIC_MEDIA", "ratio: \"1:1\"" in body, "favicon block must be 1:1")
        audit.require("PUBLIC_MEDIA", "width: 1024" in body, "favicon block width must be 1024")
        audit.require("PUBLIC_MEDIA", "height: 1024" in body, "favicon block height must be 1024")

    og_block = re.search(r"\n  og_image:\n(?P<body>(?:    .+\n)+)", txt)
    audit.require("PUBLIC_MEDIA", og_block is not None, "public-media missing og_image block")
    if og_block:
        body = og_block.group("body")
        audit.require("PUBLIC_MEDIA", "final_path: \"/assets/media/app/hero-final.jpg\"" in body, "og_image block must point to hero-final.jpg")
        audit.require("PUBLIC_MEDIA", "ratio: \"1024:500\"" in body, "og_image block ratio must be 1024:500")
        audit.require("PUBLIC_MEDIA", "width: 1024" in body, "og_image block width must be 1024")
        audit.require("PUBLIC_MEDIA", "height: 500" in body, "og_image block height must be 500")

    head = read("docs/_includes/head-custom.html")
    manifest = read("docs/site.webmanifest")

    for bad in ["favicon-32.png", "favicon-16.png", "apple-touch-icon.png", "favicon_32", "favicon_16", "apple_touch"]:
        audit.require("PUBLIC_MEDIA", bad not in head, f"head-custom must not reference {bad}")
        audit.require("PUBLIC_MEDIA", bad not in manifest, f"site.webmanifest must not reference {bad}")

    audit.require("PUBLIC_MEDIA", "logo-final.png" in manifest or "icon_src" in manifest, "manifest must use registry icon")
    audit.require("PUBLIC_MEDIA", "sizes\": \"1024x1024\"" in manifest, "manifest icon size must be 1024x1024")


def validate_gallery(audit: Audit) -> None:
    es = read("docs/gallery.md")
    en = read("docs/en/gallery.md")
    registry = read("docs/_data/gallery-media.yml")

    for txt, rel in [(es, "docs/gallery.md"), (en, "docs/en/gallery.md")]:
        audit.require("GALLERY", "slot_overview_a" in txt, f"{rel} must show slot_overview_a")
        audit.require("GALLERY", "slot_carriage_a" in txt, f"{rel} must show slot_carriage_a")
        audit.require("GALLERY", "slot_carriage_b" in txt, f"{rel} must show slot_carriage_b")
        audit.require("GALLERY", "slot_overview_b" not in txt, f"{rel} must not show duplicate slot_overview_b")

    for slot in ["slot_overview_a", "slot_overview_b", "slot_carriage_a", "slot_carriage_b"]:
        audit.require("GALLERY", f"{slot}:" in registry, f"gallery-media missing {slot}")

    audit.require("GALLERY", "slot_belt_a:" not in registry, "gallery-media must not expose pending slot_belt_a")
    audit.require("GALLERY", "slot_belt_b:" not in registry, "gallery-media must not expose pending slot_belt_b")
    audit.require("GALLERY", "slot_electronics:" not in registry, "gallery-media must not expose pending slot_electronics")
    audit.require("GALLERY", "slot_endstop_x:" not in registry, "gallery-media must not expose pending slot_endstop_x")
    audit.require("GALLERY", "slot_phone_mount:" not in registry, "gallery-media must not expose pending slot_phone_mount")


def validate_downloads(audit: Audit) -> None:
    for rel in ["docs/downloads.md", "docs/en/downloads.md"]:
        txt = read(rel)

        audit.require("DOWNLOADS", "raw_stl_base" in txt, f"{rel} must define raw_stl_base")
        audit.require("DOWNLOADS", "raw_bom_base" in txt, f"{rel} must define raw_bom_base")
        audit.require("DOWNLOADS", "tree_stl_base" in txt, f"{rel} must define tree_stl_base")
        audit.require("DOWNLOADS", "site.raw_base }}/prints/STL" not in txt, f"{rel} must not use site.raw_base for STL links")
        audit.require("DOWNLOADS", "slider-odos3d-lab-stl-pack-v1.zip" in txt, f"{rel} must keep ZIP placeholder")

        for name in STL_NAMES:
            audit.require("DOWNLOADS", name in txt, f"{rel} missing STL link: {name}")

    audit.require("DOWNLOADS", not path("docs/assets/downloads/slider-odos3d-lab-stl-pack-v1.zip").exists(), "ZIP should not exist unless owner uploads it")


def validate_sitemap(audit: Audit) -> None:
    txt = read("docs/sitemap.xml")

    for route in PUBLIC_PAGES:
        if route in {"/404.html"}:
            continue
        audit.require("SITEMAP", f"{route}</loc>" in txt, f"sitemap missing public route {route}")

    for route in FORBIDDEN_PUBLIC_ROUTES_IN_SITEMAP:
        audit.require("SITEMAP", route not in txt, f"sitemap must not include internal/redirect route {route}")

    for bad in [".png", ".jpg", ".jpeg", ".svg", ".stl", ".zip"]:
        audit.require("SITEMAP", bad not in txt.lower(), f"sitemap must not include asset pattern {bad}")


def validate_legal(audit: Audit) -> None:
    for rel in [
        "docs/privacy-policy.md",
        "docs/terms.md",
        "docs/en/privacy-policy.md",
        "docs/en/terms.md",
    ]:
        txt = read(rel)
        fm = parse_front_matter(rel)

        audit.require("LEGAL", fm.get("layout") == "public-page", f"{rel} must use public-page")
        audit.require("LEGAL", "odos3d.Lab@gmail.com" in txt or "identity.support_email" in txt, f"{rel} should expose support/legal email")
        audit.require("LEGAL", "odos3d@gmail.com" not in txt, f"{rel} must not contain old email")


def validate_no_old_public_artifacts(audit: Audit) -> None:
    scanned = text_files()

    for p in scanned:
        rel = p.relative_to(ROOT).as_posix()
        if rel == "scripts/public_site_audit.py":
            continue
        txt = p.read_text(encoding="utf-8", errors="ignore")

        if "odos3d@gmail.com" in txt:
            audit.fail("OLD_ARTIFACTS", f"Old email found in {rel}")

        if "electroniica" in txt or "Labtapa" in txt:
            audit.fail("OLD_ARTIFACTS", f"Old STL typo found in {rel}")

        if "{% include topnav.html %}" in txt:
            if rel != "docs/internal/README.md":
                audit.fail("OLD_ARTIFACTS", f"Executable topnav include found in {rel}")

    for rel in [
        "docs/_includes/head-custom.html",
        "docs/site.webmanifest",
        "docs/_data/public-media.yml",
    ]:
        txt = read(rel)
        audit.require("OLD_ARTIFACTS", "favicon-final.png" not in txt, f"{rel} must not publicly use favicon-final.png")
        audit.require("OLD_ARTIFACTS", "og-home-final.jpg" not in txt, f"{rel} must not publicly use og-home-final.jpg")
        audit.require("OLD_ARTIFACTS", "hero-final.png" not in txt, f"{rel} must not use old hero-final.png")


def validate_asset_status(audit: Audit) -> None:
    txt = read("docs/_data/asset-status.yml")

    audit.require("ASSET_STATUS", "asset_key: favicon" in txt, "asset-status missing favicon")
    audit.require("ASSET_STATUS", "final_filename: logo-final.png" in txt, "asset-status favicon must use logo-final.png")
    audit.require("ASSET_STATUS", "asset_key: og_image" in txt, "asset-status missing og_image")
    audit.require("ASSET_STATUS", "final_filename: hero-final.jpg" in txt, "asset-status og_image must use hero-final.jpg")

    for key in ["belt_a", "belt_b", "electronics", "endstop_x", "phone_mount"]:
        pattern = rf"asset_key: {key}[\s\S]*?status: pending"
        audit.require("ASSET_STATUS", re.search(pattern, txt) is not None, f"asset-status {key} must remain pending")


def main() -> int:
    audit = Audit()

    validate_files_exist(audit)
    validate_routes(audit)
    validate_public_pages(audit)
    validate_redirects(audit)
    validate_public_links(audit)
    validate_public_media(audit)
    validate_gallery(audit)
    validate_downloads(audit)
    validate_sitemap(audit)
    validate_legal(audit)
    validate_asset_status(audit)
    validate_no_old_public_artifacts(audit)

    return audit.summary()


if __name__ == "__main__":
    sys.exit(main())
