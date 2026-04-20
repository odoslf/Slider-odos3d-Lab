#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_CANONICAL_MAP = {
    "/": "docs/index.html",
    "/hardware/": "docs/index.md",
    "/downloads/": "docs/downloads.md",
    "/support/": "docs/support.md",
    "/gallery/": "docs/gallery.md",
    "/privacy-policy/": "docs/privacy-policy.md",
    "/terms/": "docs/terms.md",
    "/en/": "docs/en/index.html",
    "/en/hardware/": "docs/en/hardware.md",
    "/en/downloads/": "docs/en/downloads.md",
    "/en/support/": "docs/en/support.md",
    "/en/gallery/": "docs/en/gallery.md",
    "/en/privacy-policy/": "docs/en/privacy-policy.md",
    "/en/terms/": "docs/en/terms.md",
    "/smart-timelapse-ai/": "docs/smart-timelapse-ai/index.html",
    "/en/smart-timelapse-ai/": "docs/en/smart-timelapse-ai/index.html",
}


FROZEN_TARGET_FILENAMES = {
    "logo": "logo-final.svg",
    "hero": "hero-final.jpg",
    "slider_mobile": "slider-mobile-final.jpg",
    "slider_dslr": "slider-dslr-final.jpg",
    "app_screenshot": "app-screenshot-final.png",
    "video_thumb": "video-thumb-final.jpg",
    "favicon": "favicon-final.svg",
    "og_image": "og-home-final.jpg",
}

CANONICAL_PAGES = [
    "docs/index.html",
    "docs/index.md",
    "docs/downloads.md",
    "docs/support.md",
    "docs/gallery.md",
    "docs/privacy-policy.md",
    "docs/terms.md",
    "docs/en/index.html",
    "docs/en/hardware.md",
    "docs/en/downloads.md",
    "docs/en/support.md",
    "docs/en/gallery.md",
    "docs/en/privacy-policy.md",
    "docs/en/terms.md",
]

CRITICAL_FILES = [
    "docs/_data/public-links.yml",
    "docs/_data/public-media.yml",
    "docs/_includes/public-media-item.html",
    "docs/_includes/public-video-card.html",
    "docs/_includes/public-site-header.html",
    "docs/_includes/public-site-footer.html",
    "docs/_includes/public-lang-switch.html",
    "docs/_includes/gallery-media-item.html",
    "docs/_layouts/public-page.html",
    "docs/assets/css/public-shell.css",
    "docs/assets/css/public-pages.css",
    "docs/assets/css/smart-timelapse-home.css",
    "docs/robots.txt",
    "docs/sitemap.xml",
    "docs/llms.txt",
    "docs/site.webmanifest",
    "docs/404.html",
    "docs/_data/gallery-media.yml",
    "docs/_data/asset-status.yml",
    "docs/ASSET_REQUEST_ORDER.md",
    "docs/GALLERY_INGESTION_GUIDE.md",
    "docs/assets/media/gallery/.gitkeep",
    "docs/gallery.md",
    "docs/en/gallery.md",
    "docs/smart-timelapse-ai/index.html",
    "docs/en/smart-timelapse-ai/index.html",
]

APP_ASSET_KEYS = [
    "logo",
    "hero",
    "app_screenshot",
    "slider_mobile",
    "slider_dslr",
    "video_thumb",
    "favicon",
    "og_image",
]

GALLERY_ASSET_KEYS = [
    "slot_overview_a",
    "slot_overview_b",
    "slot_carriage_a",
    "slot_carriage_b",
    "slot_belt_a",
    "slot_belt_b",
    "slot_electronics",
    "slot_endstop_x",
    "slot_phone_mount",
]

ASSET_STATUS_REQUIRED_FIELDS = [
    "asset_key",
    "family",
    "final_filename",
    "final_directory",
    "source_registry",
    "source_slot_key",
    "public_usage",
    "priority",
    "request_order",
    "status",
    "requested_from_user",
    "file_received",
    "uploaded_to_repo",
    "activated_in_yaml",
    "notes",
]

GALLERY_SLOT_KEYS = [
    "slot_overview_a",
    "slot_overview_b",
    "slot_carriage_a",
    "slot_carriage_b",
    "slot_belt_a",
    "slot_belt_b",
    "slot_electronics",
    "slot_endstop_x",
    "slot_phone_mount",
]

GALLERY_FROZEN_FILENAMES = {
    "slot_overview_a": "slider-gallery-01-overview-a.jpg",
    "slot_overview_b": "slider-gallery-02-overview-b.jpg",
    "slot_carriage_a": "slider-gallery-03-carriage-a.jpg",
    "slot_carriage_b": "slider-gallery-04-carriage-b.jpg",
    "slot_belt_a": "slider-gallery-05-belt-a.jpg",
    "slot_belt_b": "slider-gallery-06-belt-b.jpg",
    "slot_electronics": "slider-gallery-07-electronics.jpg",
    "slot_endstop_x": "slider-gallery-08-endstop-x.jpg",
    "slot_phone_mount": "slider-gallery-09-phone-mount.jpg",
}

HARD_CODE_PATTERNS = {
    "odos3d.Lab@gmail.com": ["odos3d.Lab@gmail.com"],
    "Silvia Díaz Celaya": ["Silvia Díaz Celaya"],
    "github repo absolute": ["https://github.com/odoslf/Slider-odos3d-Lab"],
    "app-hero-slot": ["/assets/img/app-hero-slot.svg", "docs/assets/img/app-hero-slot.svg"],
    "app-gallery-slider-mobile-slot": ["/assets/img/app-gallery-slider-mobile-slot.svg", "docs/assets/img/app-gallery-slider-mobile-slot.svg"],
    "app-gallery-slider-dslr-slot": ["/assets/img/app-gallery-slider-dslr-slot.svg", "docs/assets/img/app-gallery-slider-dslr-slot.svg"],
    "app-gallery-app-screenshot-slot": ["/assets/img/app-gallery-app-screenshot-slot.svg", "docs/assets/img/app-gallery-app-screenshot-slot.svg"],
    "app-video-slot": ["/assets/img/app-video-slot.svg", "docs/assets/img/app-video-slot.svg"],
    "app-logo-slot": ["/assets/img/app-logo-slot.svg", "docs/assets/img/app-logo-slot.svg"],
    "favicon-slot": ["/assets/img/favicon-slot.svg", "docs/assets/img/favicon-slot.svg"],
    "og-home-slot": ["/assets/img/og-home-slot.svg", "docs/assets/img/og-home-slot.svg"],
}

HARD_CODE_ALLOWED_FILES = {
    "docs/_data/public-links.yml",
    "docs/_data/public-media.yml",
    "docs/smart-timelapse-ai/ASSET_SLOTS.md",
    "docs/_includes/public-media-item.html",
    "docs/_includes/public-video-card.html",
    "docs/_includes/public-site-header.html",
    "docs/_includes/public-site-footer.html",
    "docs/_includes/head-custom.html",
}


class Audit:
    def __init__(self) -> None:
        self.errors: Dict[str, List[str]] = {}

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
        total = sum(len(v) for v in self.errors.values())
        for category in sorted(self.errors.keys()):
            print(f"\n[{category}] {len(self.errors[category])} issue(s)")
            for item in self.errors[category]:
                print(f" - {item}")
        print(f"\nFAIL ({total} issue(s))")
        return 1


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def parse_front_matter(rel: str) -> Dict[str, str]:
    text = read_text(rel)
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        return {}
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}
    data: Dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def parse_simple_yaml(rel: str) -> Dict[str, Any]:
    text = read_text(rel)
    root: Dict[str, Any] = {}
    stack: List[Tuple[int, Dict[str, Any]]] = [(-1, root)]

    for lineno, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw.strip()
        if ":" not in stripped:
            raise ValueError(f"Unsupported YAML at {rel}:{lineno}: {raw}")

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        if not stack:
            raise ValueError(f"YAML indentation error at {rel}:{lineno}")

        parent = stack[-1][1]
        if value == "":
            obj: Dict[str, Any] = {}
            parent[key] = obj
            stack.append((indent, obj))
        else:
            parsed: Any = value
            if parsed.startswith('"') and parsed.endswith('"'):
                parsed = parsed[1:-1]
            elif parsed.startswith("'") and parsed.endswith("'"):
                parsed = parsed[1:-1]
            elif parsed.lower() == "true":
                parsed = True
            elif parsed.lower() == "false":
                parsed = False
            elif re.fullmatch(r"[0-9]+", parsed):
                parsed = int(parsed)
            parent[key] = parsed
    return root


def parse_ordered_list_yaml(rel: str) -> Dict[str, List[Dict[str, Any]]]:
    text = read_text(rel)
    data: Dict[str, List[Dict[str, Any]]] = {}
    current_section: str | None = None
    current_item: Dict[str, Any] | None = None

    def parse_scalar(value: str) -> Any:
        val = value.strip()
        if val.startswith('"') and val.endswith('"'):
            return val[1:-1]
        if val.startswith("'") and val.endswith("'"):
            return val[1:-1]
        if val.lower() == "true":
            return True
        if val.lower() == "false":
            return False
        if re.fullmatch(r"[0-9]+", val):
            return int(val)
        return val

    for lineno, raw in enumerate(text.splitlines(), start=1):
        if not raw.strip() or raw.strip().startswith("#"):
            continue

        if raw.endswith(":") and not raw.startswith(" "):
            section = raw[:-1].strip()
            data[section] = []
            current_section = section
            current_item = None
            continue

        if raw.startswith("  - "):
            if current_section is None:
                raise ValueError(f"List item outside section at {rel}:{lineno}")
            kv = raw[4:]
            if ":" not in kv:
                raise ValueError(f"Invalid list item key/value at {rel}:{lineno}")
            key, value = kv.split(":", 1)
            current_item = {key.strip(): parse_scalar(value)}
            data[current_section].append(current_item)
            continue

        if raw.startswith("    "):
            if current_item is None:
                raise ValueError(f"Field outside list item at {rel}:{lineno}")
            kv = raw.strip()
            if ":" not in kv:
                raise ValueError(f"Invalid field at {rel}:{lineno}")
            key, value = kv.split(":", 1)
            current_item[key.strip()] = parse_scalar(value)
            continue

        raise ValueError(f"Unsupported YAML structure at {rel}:{lineno}: {raw}")

    return data


def all_docs_files() -> List[Path]:
    out: List[Path] = []
    for p in (ROOT / "docs").rglob("*"):
        if p.is_file():
            out.append(p)
    return out


def validate_critical_files(audit: Audit) -> None:
    for rel in CRITICAL_FILES:
        audit.require("CRITICAL_FILES", (ROOT / rel).exists(), f"Missing critical file: {rel}")


def validate_public_links(audit: Audit) -> Dict[str, Any]:
    data = parse_simple_yaml("docs/_data/public-links.yml")
    required = {
        "site_identity": ["product_name", "product_name_short", "support_email", "legal_responsible_name"],
        "external_links": ["github_repo", "github_pages_base", "youtube_url", "play_store_url"],
        "internal_routes_es": ["home", "hardware", "downloads", "support", "gallery", "privacy", "terms"],
        "internal_routes_en": ["home", "hardware", "downloads", "support", "gallery", "privacy", "terms"],
        "flags": ["has_play_store", "has_youtube"],
    }
    for section, keys in required.items():
        audit.require("PUBLIC_LINKS", section in data and isinstance(data[section], dict), f"Missing section {section}")
        if section in data and isinstance(data[section], dict):
            for k in keys:
                audit.require("PUBLIC_LINKS", k in data[section], f"Missing key {section}.{k}")

    site = data.get("site_identity", {})
    ext = data.get("external_links", {})
    flags = data.get("flags", {})

    audit.require("PUBLIC_LINKS", site.get("support_email") == "odos3d.Lab@gmail.com", "support_email must be odos3d.Lab@gmail.com")
    audit.require("PUBLIC_LINKS", site.get("legal_responsible_name") == "Silvia Díaz Celaya", "legal_responsible_name must be Silvia Díaz Celaya")
    audit.require("PUBLIC_LINKS", bool(ext.get("github_repo", "").strip()), "external_links.github_repo must not be empty")
    audit.require("PUBLIC_LINKS", bool(ext.get("github_pages_base", "").strip()), "external_links.github_pages_base must not be empty")

    if flags.get("has_youtube") is True:
        audit.require("PUBLIC_LINKS", bool(str(ext.get("youtube_url", "")).strip()), "has_youtube=true requires external_links.youtube_url")
    if flags.get("has_play_store") is True:
        audit.require("PUBLIC_LINKS", bool(str(ext.get("play_store_url", "")).strip()), "has_play_store=true requires external_links.play_store_url")

    return data


def validate_public_media(audit: Audit) -> Dict[str, Any]:
    data = parse_simple_yaml("docs/_data/public-media.yml")
    site_media = data.get("site_media", {}) if isinstance(data.get("site_media"), dict) else {}
    required_blocks = ["logo", "hero", "slider_mobile", "slider_dslr", "app_screenshot", "video_thumb", "favicon", "og_image"]
    for b in required_blocks:
        audit.require("PUBLIC_MEDIA", b in site_media and isinstance(site_media[b], dict), f"Missing media block {b}")

    req_fields = [
        "placeholder_path", "final_path", "active_source", "is_placeholder", "alt_es", "alt_en", "caption_es", "caption_en",
        "kind", "ratio", "width", "height", "loading_default",
        "target_filename", "target_directory", "preferred_format",
        "recommended_min_width", "recommended_min_height", "crop_strategy",
        "safe_area_notes", "transparency_required", "used_on_pages",
        "used_in_sections", "current_slot_source",
    ]
    for b in required_blocks:
        block = site_media.get(b, {})
        if not isinstance(block, dict):
            continue
        for f in req_fields:
            audit.require("PUBLIC_MEDIA", f in block, f"Missing {b}.{f}")

        placeholder_path = str(block.get("placeholder_path", "")).strip()
        final_path = str(block.get("final_path", "")).strip()
        active_source = str(block.get("active_source", "")).strip()

        audit.require("PUBLIC_MEDIA", active_source in {"placeholder", "final"}, f"{b}.active_source must be placeholder/final")

        if placeholder_path.startswith("/") and not placeholder_path.startswith("//"):
            local = placeholder_path.lstrip("/")
            audit.require("PUBLIC_MEDIA", (ROOT / "docs" / local).exists(), f"Placeholder path not found for {b}: {placeholder_path}")

        expected_final_path = f"/assets/media/app/{FROZEN_TARGET_FILENAMES[b]}"
        audit.require("PUBLIC_MEDIA", final_path == expected_final_path, f"{b}.final_path must be {expected_final_path}")

        if active_source == "placeholder":
            audit.require("PUBLIC_MEDIA", block.get("is_placeholder") is True, f"{b}.is_placeholder must be true when active_source=placeholder")
        elif active_source == "final":
            if final_path.startswith("/") and not final_path.startswith("//"):
                local = final_path.lstrip("/")
                audit.require("PUBLIC_MEDIA", (ROOT / "docs" / local).exists(), f"Final path not found for {b}: {final_path}")
            audit.require("PUBLIC_MEDIA", block.get("is_placeholder") is False, f"{b}.is_placeholder must be false when active_source=final")

        audit.require("PUBLIC_MEDIA", str(block.get("alt_es", "")).strip() != "", f"{b}.alt_es must not be empty")
        audit.require("PUBLIC_MEDIA", str(block.get("alt_en", "")).strip() != "", f"{b}.alt_en must not be empty")
        audit.require("PUBLIC_MEDIA", str(block.get("kind", "")).strip() != "", f"{b}.kind must not be empty")
        audit.require("PUBLIC_MEDIA", str(block.get("ratio", "")).strip() != "", f"{b}.ratio must not be empty")

        width = block.get("width")
        height = block.get("height")
        audit.require("PUBLIC_MEDIA", isinstance(width, int) and width > 0, f"{b}.width must be positive int")
        audit.require("PUBLIC_MEDIA", isinstance(height, int) and height > 0, f"{b}.height must be positive int")
        audit.require("PUBLIC_MEDIA", str(block.get("loading_default", "")).strip() in {"lazy", "eager"}, f"{b}.loading_default must be lazy/eager")

        rec_w = block.get("recommended_min_width")
        rec_h = block.get("recommended_min_height")
        audit.require("PUBLIC_MEDIA", isinstance(rec_w, int) and rec_w > 0, f"{b}.recommended_min_width must be positive int")
        audit.require("PUBLIC_MEDIA", isinstance(rec_h, int) and rec_h > 0, f"{b}.recommended_min_height must be positive int")

        audit.require("PUBLIC_MEDIA", str(block.get("target_directory", "")).strip() == "docs/assets/media/app/", f"{b}.target_directory must be docs/assets/media/app/")
        audit.require("PUBLIC_MEDIA", str(block.get("target_filename", "")).strip() == FROZEN_TARGET_FILENAMES[b], f"{b}.target_filename must be {FROZEN_TARGET_FILENAMES[b]}")
        expected_by_target = "/assets/media/app/" + str(block.get("target_filename", "")).strip()
        audit.require("PUBLIC_MEDIA", final_path == expected_by_target, f"{b}.final_path must match target_directory + target_filename")
        audit.require("PUBLIC_MEDIA", str(block.get("used_on_pages", "")).strip() != "", f"{b}.used_on_pages must not be empty")
        audit.require("PUBLIC_MEDIA", "path" not in block, f"{b}.path legacy field should not exist")

    video = site_media.get("video_thumb", {})
    audit.require("PUBLIC_MEDIA", "youtube_url_source" in video and str(video.get("youtube_url_source", "")).strip() != "", "video_thumb.youtube_url_source is required")
    return data


def validate_gallery_media(audit: Audit) -> Dict[str, Any]:
    data = parse_simple_yaml("docs/_data/gallery-media.yml")
    gallery_media = data.get("gallery_media", {}) if isinstance(data.get("gallery_media"), dict) else {}
    for key in GALLERY_SLOT_KEYS:
        audit.require("GALLERY_MEDIA", key in gallery_media and isinstance(gallery_media[key], dict), f"Missing gallery slot {key}")

    required_fields = [
        "placeholder_path", "final_path", "active_source", "target_filename", "target_directory",
        "alt_es", "alt_en", "caption_es", "caption_en", "section_es", "section_en", "ratio", "width", "height",
    ]

    for key in GALLERY_SLOT_KEYS:
        slot = gallery_media.get(key, {})
        if not isinstance(slot, dict):
            continue
        for field in required_fields:
            audit.require("GALLERY_MEDIA", field in slot, f"Missing {key}.{field}")

        target_directory = str(slot.get("target_directory", "")).strip()
        target_filename = str(slot.get("target_filename", "")).strip()
        final_path = str(slot.get("final_path", "")).strip()
        placeholder_path = str(slot.get("placeholder_path", "")).strip()
        active_source = str(slot.get("active_source", "")).strip()

        audit.require("GALLERY_MEDIA", active_source in {"placeholder", "final"}, f"{key}.active_source must be placeholder/final")
        audit.require("GALLERY_MEDIA", target_directory == "docs/assets/media/gallery/", f"{key}.target_directory must be docs/assets/media/gallery/")
        audit.require("GALLERY_MEDIA", target_filename == GALLERY_FROZEN_FILENAMES[key], f"{key}.target_filename must be {GALLERY_FROZEN_FILENAMES[key]}")
        audit.require("GALLERY_MEDIA", final_path == f"/assets/media/gallery/{GALLERY_FROZEN_FILENAMES[key]}", f"{key}.final_path must match frozen filename in gallery folder")

        if placeholder_path.startswith("/") and not placeholder_path.startswith("//"):
            local_placeholder = placeholder_path.lstrip("/")
            audit.require("GALLERY_MEDIA", (ROOT / "docs" / local_placeholder).exists(), f"Placeholder path not found for {key}: {placeholder_path}")
        if active_source == "final" and final_path.startswith("/") and not final_path.startswith("//"):
            local_final = final_path.lstrip("/")
            audit.require("GALLERY_MEDIA", (ROOT / "docs" / local_final).exists(), f"Final path not found for {key}: {final_path}")

        width = slot.get("width")
        height = slot.get("height")
        audit.require("GALLERY_MEDIA", isinstance(width, int) and width > 0, f"{key}.width must be positive int")
        audit.require("GALLERY_MEDIA", isinstance(height, int) and height > 0, f"{key}.height must be positive int")

    return data


def validate_routes(audit: Audit) -> None:
    seen: Dict[str, List[str]] = {}
    for p in all_docs_files():
        if p.suffix not in {".md", ".html"}:
            continue
        rel = p.relative_to(ROOT).as_posix()
        fm = parse_front_matter(rel)
        if "permalink" in fm:
            seen.setdefault(fm["permalink"], []).append(rel)

    for route, expected_file in EXPECTED_CANONICAL_MAP.items():
        audit.require("ROUTES", route in seen, f"Missing route {route}")
        if route in seen:
            audit.require("ROUTES", expected_file in seen[route], f"Route {route} must map to {expected_file}, found {seen[route]}")
            audit.require("ROUTES", len(seen[route]) == 1, f"Route {route} has duplicate sources: {seen[route]}")

    audit.require("ROUTES", EXPECTED_CANONICAL_MAP["/"] == "docs/index.html", "Internal invariant: / must come from docs/index.html")


def validate_redirects(audit: Audit) -> None:
    es = read_text("docs/smart-timelapse-ai/index.html")
    en = read_text("docs/en/smart-timelapse-ai/index.html")

    audit.require("REDIRECTS", "noindex" in es.lower(), "ES redirect must include noindex")
    audit.require("REDIRECTS", "noindex" in en.lower(), "EN redirect must include noindex")
    audit.require("REDIRECTS", "internal_routes_es.home" in es and "window.location.replace" in es, "ES redirect must target /")
    audit.require("REDIRECTS", "internal_routes_en.home" in en and "window.location.replace" in en, "EN redirect must target /en/")

    sitemap = read_text("docs/sitemap.xml")
    audit.require("REDIRECTS", "/smart-timelapse-ai/" not in sitemap, "sitemap must not include /smart-timelapse-ai/")
    audit.require("REDIRECTS", "/en/smart-timelapse-ai/" not in sitemap, "sitemap must not include /en/smart-timelapse-ai/")


def validate_sitemap(audit: Audit) -> None:
    text = read_text("docs/sitemap.xml")
    expected = [
        "/", "/hardware/", "/downloads/", "/support/", "/gallery/", "/privacy-policy/", "/terms/",
        "/en/", "/en/hardware/", "/en/downloads/", "/en/support/", "/en/gallery/", "/en/privacy-policy/", "/en/terms/",
    ]
    for route in expected:
        audit.require("SITEMAP", f"{route}</loc>" in text, f"sitemap missing route {route}")

    forbidden = ["/smart-timelapse-ai/", "/en/smart-timelapse-ai/", "/assets/", ".png", ".jpg", ".svg"]
    for frag in forbidden:
        audit.require("SITEMAP", frag not in text, f"sitemap contains forbidden entry pattern: {frag}")


def validate_robots(audit: Audit) -> None:
    text = read_text("docs/robots.txt")
    low = text.lower()
    audit.require("ROBOTS", "user-agent: *" in low, "robots.txt missing User-agent: *")
    audit.require("ROBOTS", "allow: /" in low, "robots.txt missing Allow: /")
    audit.require("ROBOTS", "sitemap:" in low, "robots.txt missing Sitemap")
    audit.require("ROBOTS", "/sitemap.xml" in low or "{{ site.url }}{{ site.baseurl }}/sitemap.xml" in text, "robots sitemap must reference real sitemap URL")


def validate_hardcodes(audit: Audit) -> None:
    audit_scope = {
        *CANONICAL_PAGES,
        "docs/_includes/head-custom.html",
        "docs/_includes/public-site-header.html",
        "docs/_includes/public-site-footer.html",
        "docs/_includes/public-lang-switch.html",
        "docs/_includes/public-media-item.html",
        "docs/_includes/public-video-card.html",
        "docs/_layouts/public-page.html",
        "docs/404.html",
        "docs/site.webmanifest",
        "docs/smart-timelapse-ai/index.html",
        "docs/en/smart-timelapse-ai/index.html",
        "docs/smart-timelapse-ai/ASSET_SLOTS.md",
        "docs/robots.txt",
        "docs/sitemap.xml",
        "docs/llms.txt",
    }

    for rel in sorted(audit_scope):
        path = ROOT / rel
        if not path.exists() or rel in HARD_CODE_ALLOWED_FILES:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        for label, tokens in HARD_CODE_PATTERNS.items():
            for token in tokens:
                if token and token in content:
                    audit.fail("HARDCODES", f"Hardcoded '{label}' found in {rel}")
                    break


def validate_bilingual(audit: Audit) -> None:
    for rel in CANONICAL_PAGES:
        fm = parse_front_matter(rel)
        if rel in {"docs/index.html", "docs/en/index.html"}:
            continue
        audit.require("BILINGUAL", "lang_page" in fm and fm.get("lang_page", "").strip() != "", f"{rel} missing lang_page")
        audit.require("BILINGUAL", "alt_url" in fm and fm.get("alt_url", "").strip() != "", f"{rel} missing alt_url")

    header = read_text("docs/_includes/public-site-header.html")
    audit.require("BILINGUAL", "public-lang-switch.html" in header, "Header must include language switch")


def validate_metadata(audit: Audit) -> None:
    for rel in CANONICAL_PAGES:
        fm = parse_front_matter(rel)
        if rel in {"docs/index.html", "docs/en/index.html"}:
            text = read_text(rel)
            audit.require("METADATA", "<title>" in text and "meta name=\"description\"" in text, f"{rel} missing title/description in source")
            continue
        audit.require("METADATA", "title" in fm and fm.get("title", "").strip() != "", f"{rel} missing title")
        audit.require("METADATA", "description" in fm and fm.get("description", "").strip() != "", f"{rel} missing description")

    head = read_text("docs/_includes/head-custom.html")
    checks = [
        "rel=\"canonical\"",
        "hreflang",
        "og:title",
        "og:description",
        "twitter:title",
        "twitter:description",
    ]
    for c in checks:
        audit.require("METADATA", c in head, f"head-custom missing {c}")


def validate_media_registry_usage(audit: Audit) -> None:
    es_home = read_text("docs/index.html")
    en_home = read_text("docs/en/index.html")
    forbidden_tokens = [
        "/assets/img/app-hero-slot.svg",
        "/assets/img/app-gallery-slider-mobile-slot.svg",
        "/assets/img/app-gallery-slider-dslr-slot.svg",
        "/assets/img/app-gallery-app-screenshot-slot.svg",
        "/assets/img/app-video-slot.svg",
        "/assets/img/app-logo-slot.svg",
        "/assets/img/favicon-slot.svg",
        "/assets/img/og-home-slot.svg",
    ]
    for token in forbidden_tokens:
        audit.require("MEDIA_REGISTRY", token not in es_home, f"Home ES references direct media path: {token}")
        audit.require("MEDIA_REGISTRY", token not in en_home, f"Home EN references direct media path: {token}")

    header = read_text("docs/_includes/public-site-header.html")
    footer = read_text("docs/_includes/public-site-footer.html")
    audit.require("MEDIA_REGISTRY", "site.data.public-media" in header, "Header must source media from registry")
    audit.require("MEDIA_REGISTRY", "site.data.public-media" in footer, "Footer must source media from registry")
    audit.require("MEDIA_REGISTRY", "public-media-item.html" in es_home and "public-video-card.html" in es_home, "Home ES must use media/video includes")
    audit.require("MEDIA_REGISTRY", "public-media-item.html" in en_home and "public-video-card.html" in en_home, "Home EN must use media/video includes")


def validate_gallery_integration(audit: Audit) -> None:
    es_gallery = read_text("docs/gallery.md")
    en_gallery = read_text("docs/en/gallery.md")
    gallery_include = read_text("docs/_includes/gallery-media-item.html")
    links_data = read_text("docs/_data/public-links.yml")
    targets = [
        "docs/index.md",
        "docs/downloads.md",
        "docs/support.md",
        "docs/en/hardware.md",
        "docs/en/downloads.md",
        "docs/en/support.md",
    ]

    audit.require("GALLERY_INTEGRATION", "layout: public-page" in es_gallery, "docs/gallery.md must use public-page layout")
    audit.require("GALLERY_INTEGRATION", "layout: public-page" in en_gallery, "docs/en/gallery.md must use public-page layout")
    audit.require("GALLERY_INTEGRATION", "gallery-media-item.html" in es_gallery, "docs/gallery.md must use gallery-media-item include")
    audit.require("GALLERY_INTEGRATION", "gallery-media-item.html" in en_gallery, "docs/en/gallery.md must use gallery-media-item include")
    audit.require("GALLERY_INTEGRATION", "site.data.gallery-media.gallery_media" in gallery_include, "gallery-media-item include must source data from docs/_data/gallery-media.yml")
    audit.require("GALLERY_INTEGRATION", "/gallery/" in links_data and "/en/gallery/" in links_data, "public-links must include gallery routes")

    linked_pages = 0
    for rel in targets:
        text = read_text(rel)
        if "routes.gallery" in text or "/gallery/" in text or "/en/gallery/" in text:
            linked_pages += 1
    audit.require("GALLERY_INTEGRATION", linked_pages >= 4, "Hardware/downloads/support pages must include gallery links in both languages")

    forbidden_tokens = [
        "raw.githubusercontent.com",
        "site.raw_base }}/images/gallery/",
        "/images/gallery/",
    ]
    for token in forbidden_tokens:
        audit.require("GALLERY_INTEGRATION", token not in es_gallery, f"docs/gallery.md contains forbidden legacy token: {token}")
        audit.require("GALLERY_INTEGRATION", token not in en_gallery, f"docs/en/gallery.md contains forbidden legacy token: {token}")


def validate_asset_status_master(audit: Audit) -> None:
    status_data = parse_ordered_list_yaml("docs/_data/asset-status.yml")
    app_items = status_data.get("app_assets", [])
    gallery_items = status_data.get("gallery_assets", [])

    audit.require("ASSET_STATUS", isinstance(app_items, list), "asset-status.yml must include app_assets list")
    audit.require("ASSET_STATUS", isinstance(gallery_items, list), "asset-status.yml must include gallery_assets list")

    app_by_key = {str(item.get("asset_key", "")).strip(): item for item in app_items if isinstance(item, dict)}
    gallery_by_key = {str(item.get("asset_key", "")).strip(): item for item in gallery_items if isinstance(item, dict)}

    for key in APP_ASSET_KEYS:
        audit.require("ASSET_STATUS", key in app_by_key, f"Missing app asset in asset-status.yml: {key}")
    for key in GALLERY_ASSET_KEYS:
        audit.require("ASSET_STATUS", key in gallery_by_key, f"Missing gallery asset in asset-status.yml: {key}")

    valid_status = {"pending", "requested", "received", "uploaded", "activated"}
    valid_priority = {"high", "medium", "low"}

    public_media = parse_simple_yaml("docs/_data/public-media.yml").get("site_media", {})
    gallery_media = parse_simple_yaml("docs/_data/gallery-media.yml").get("gallery_media", {})

    request_orders: List[int] = []
    for key, item in list(app_by_key.items()) + list(gallery_by_key.items()):
        if not isinstance(item, dict):
            continue
        for field in ASSET_STATUS_REQUIRED_FIELDS:
            audit.require("ASSET_STATUS", field in item, f"Missing field for {key}: {field}")

        family = str(item.get("family", "")).strip()
        source_registry = str(item.get("source_registry", "")).strip()
        status = str(item.get("status", "")).strip()
        priority = str(item.get("priority", "")).strip()
        final_directory = str(item.get("final_directory", "")).strip()
        source_slot_key = str(item.get("source_slot_key", "")).strip()
        order = item.get("request_order")
        final_filename = str(item.get("final_filename", "")).strip()

        audit.require("ASSET_STATUS", family in {"app", "gallery"}, f"{key}.family must be app/gallery")
        audit.require("ASSET_STATUS", source_registry in {"public-media", "gallery-media"}, f"{key}.source_registry must be public-media/gallery-media")
        audit.require("ASSET_STATUS", status in valid_status, f"{key}.status invalid: {status}")
        audit.require("ASSET_STATUS", priority in valid_priority, f"{key}.priority invalid: {priority}")
        audit.require("ASSET_STATUS", isinstance(order, int) and order > 0, f"{key}.request_order must be positive int")
        if isinstance(order, int):
            request_orders.append(order)

        for bool_field in ["requested_from_user", "file_received", "uploaded_to_repo", "activated_in_yaml"]:
            audit.require("ASSET_STATUS", isinstance(item.get(bool_field), bool), f"{key}.{bool_field} must be boolean")

        if key in APP_ASSET_KEYS:
            audit.require("ASSET_STATUS", family == "app", f"{key}.family must be app")
            audit.require("ASSET_STATUS", source_registry == "public-media", f"{key}.source_registry must be public-media")
            audit.require("ASSET_STATUS", final_directory == "docs/assets/media/app/", f"{key}.final_directory must be docs/assets/media/app/")
            audit.require("ASSET_STATUS", source_slot_key in public_media, f"{key}.source_slot_key must exist in public-media.yml")
            if source_slot_key in public_media and isinstance(public_media[source_slot_key], dict):
                target_filename = str(public_media[source_slot_key].get("target_filename", "")).strip()
                audit.require("ASSET_STATUS", final_filename == target_filename, f"{key}.final_filename must match public-media target_filename")
        if key in GALLERY_ASSET_KEYS:
            audit.require("ASSET_STATUS", family == "gallery", f"{key}.family must be gallery")
            audit.require("ASSET_STATUS", source_registry == "gallery-media", f"{key}.source_registry must be gallery-media")
            audit.require("ASSET_STATUS", final_directory == "docs/assets/media/gallery/", f"{key}.final_directory must be docs/assets/media/gallery/")
            audit.require("ASSET_STATUS", source_slot_key in gallery_media, f"{key}.source_slot_key must exist in gallery-media.yml")
            if source_slot_key in gallery_media and isinstance(gallery_media[source_slot_key], dict):
                target_filename = str(gallery_media[source_slot_key].get("target_filename", "")).strip()
                audit.require("ASSET_STATUS", final_filename == target_filename, f"{key}.final_filename must match gallery-media target_filename")

    expected_orders = list(range(1, 18))
    audit.require("ASSET_STATUS", sorted(request_orders) == expected_orders, f"request_order must cover exactly {expected_orders}")


def validate_asset_request_order_doc(audit: Audit) -> None:
    text = read_text("docs/ASSET_REQUEST_ORDER.md")
    expected_sequence = APP_ASSET_KEYS + GALLERY_ASSET_KEYS
    pos = -1
    for key in expected_sequence:
        new_pos = text.find(key, pos + 1)
        audit.require("ASSET_STATUS_DOC", new_pos != -1, f"ASSET_REQUEST_ORDER.md missing asset key: {key}")
        if new_pos != -1:
            pos = new_pos

def validate_asset_ingestion_docs(audit: Audit) -> None:
    guide_rel = "docs/ASSET_INGESTION_GUIDE.md"
    targets_rel = "docs/assets/media/app/ASSET_TARGETS.md"
    guide_path = ROOT / guide_rel
    targets_path = ROOT / targets_rel

    audit.require("ASSET_INGESTION", guide_path.exists(), f"Missing file: {guide_rel}")
    audit.require("ASSET_INGESTION", targets_path.exists(), f"Missing file: {targets_rel}")

    required_names = [
        "logo-final.svg", "hero-final.jpg", "slider-mobile-final.jpg", "slider-dslr-final.jpg",
        "app-screenshot-final.png", "video-thumb-final.jpg", "favicon-final.svg", "og-home-final.jpg",
    ]

    if guide_path.exists():
        text = guide_path.read_text(encoding="utf-8")
        for name in required_names:
            audit.require("ASSET_INGESTION", name in text, f"ASSET_INGESTION_GUIDE missing {name}")
        audit.require("ASSET_INGESTION", "active_source" in text, "ASSET_INGESTION_GUIDE must document active_source flow")

    if targets_path.exists():
        text = targets_path.read_text(encoding="utf-8")
        for name in required_names:
            audit.require("ASSET_INGESTION", name in text, f"ASSET_TARGETS missing {name}")
        audit.require("ASSET_INGESTION", "active_source" in text, "ASSET_TARGETS must mention active_source activation")


def validate_checklist(audit: Audit) -> None:
    rel = "docs/PUBLIC_SITE_RELEASE_CHECKLIST.md"
    path = ROOT / rel
    audit.require("CHECKLIST", path.exists(), f"Missing checklist file: {rel}")
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    required_phrases = [
        "logo real",
        "hero real",
        "slider mobile real",
        "slider dslr real",
        "screenshot app real",
        "video thumb real",
        "favicon real",
        "og image real",
        "YouTube real",
        "Play Store real",
        "revisión final antes de publicar",
    ]
    for phrase in required_phrases:
        audit.require("CHECKLIST", phrase.lower() in text.lower(), f"Checklist missing: {phrase}")


def main() -> int:
    audit = Audit()
    validate_critical_files(audit)
    validate_public_links(audit)
    validate_public_media(audit)
    validate_gallery_media(audit)
    validate_routes(audit)
    validate_redirects(audit)
    validate_sitemap(audit)
    validate_robots(audit)
    validate_hardcodes(audit)
    validate_bilingual(audit)
    validate_metadata(audit)
    validate_media_registry_usage(audit)
    validate_gallery_integration(audit)
    validate_asset_status_master(audit)
    validate_asset_request_order_doc(audit)
    validate_asset_ingestion_docs(audit)
    validate_checklist(audit)
    return audit.summary()


if __name__ == "__main__":
    sys.exit(main())
