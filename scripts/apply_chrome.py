#!/usr/bin/env python3
"""Apply shared head/chrome/footer to HTML pages."""
import re
from pathlib import Path

ROOT = Path("/Users/admin/satellite-ngono")
HEAD = (ROOT / "partials/head.html").read_text(encoding="utf-8")
CHROME_TOP = (ROOT / "partials/chrome-top.html").read_text(encoding="utf-8")
CHROME_FOOTER = (ROOT / "partials/chrome-footer.html").read_text(encoding="utf-8")

PAGES = [
    "index.html", "about.html", "service.html", "controle.html",
    "tarif.html", "contact.html", "booking.html", "team.html",
    "testimonial.html", "404.html", "actualite.html", "rejoindre.html",
]

INLINE_PAGES = {
    "index.html", "about.html", "service.html", "controle.html",
    "tarif.html", "contact.html",
}

PLACEHOLDER_PAGES = {
    "booking.html", "team.html", "testimonial.html", "404.html",
    "actualite.html", "rejoindre.html",
}


def replace_head(content: str) -> str:
    content = re.sub(r'<html\s+lang="[^"]*"', '<html lang="fr"', content, count=1)
    # Remove duplicate font/icon links between <head> and first library or bootstrap
    content = re.sub(
        r'(<head>.*?)(<!-- Favicon -->.*?)(<!-- Google Web Fonts -->.*?)(<!-- Icon Font Stylesheet -->.*?)(<!--.*?Libraries Stylesheet -->)',
        r'\1' + HEAD + r'\n    \5',
        content,
        count=1,
        flags=re.DOTALL,
    )
    # Fallback: if pattern failed, insert after <head>
    if "DM+Sans" not in content:
        content = re.sub(
            r"(<head>\s*)",
            r"\1" + HEAD + "\n",
            content,
            count=1,
        )
    # Strip old font awesome duplicates
    content = re.sub(
        r'\s*<link[^>]*font-awesome[^>]*>\s*',
        "\n",
        content,
        flags=re.I,
    )
    content = re.sub(
        r"\s*<link[^>]*flaticon[^>]*>\s*",
        "\n",
        content,
        flags=re.I,
    )
    content = re.sub(
        r'\s*<link href="https://fonts\.googleapis\.com/css2\?family=Barlow[^>]*>\s*',
        "\n",
        content,
    )
    if "DM+Sans" not in content:
        content = content.replace(
            "<head>",
            "<head>\n" + HEAD,
            1,
        )
    return content


def replace_chrome_top(content: str) -> str:
    pattern = re.compile(
        r"<!-- Topbar Start -->.*?<!-- Navbar End -->",
        re.DOTALL,
    )
    if pattern.search(content):
        return pattern.sub(CHROME_TOP.strip(), content, count=1)
    # Placeholder pages: after spinner
    pattern2 = re.compile(
        r"(<!-- Spinner End -->\s*)",
        re.DOTALL,
    )
    if "#topbar" in content or "#navbar" in content:
        return pattern2.sub(r"\1\n" + CHROME_TOP, content, count=1)
    return content


def replace_footer(content: str) -> str:
    pattern = re.compile(
        r"<!-- Footer Start -->.*?<!-- Footer End -->",
        re.DOTALL,
    )
    if pattern.search(content):
        return pattern.sub(CHROME_FOOTER.strip(), content, count=1)
    return content


def cleanup_scripts(content: str, name: str) -> str:
    if name in INLINE_PAGES:
        content = re.sub(r'\s*<script src="js/components\.js"></script>\s*', "\n", content)
    content = content.replace("../img/logo-sn.png", "img/logo-sn.png")
    content = content.replace('class="sr-only"', 'class="visually-hidden"')
    return content


def add_main_id(content: str) -> str:
    if 'id="main-content"' in content:
        return content
    # After chrome top / header
    markers = [
        "<!-- Carousel Start -->",
        "<!-- Page Header Start -->",
        '<div class="container-fluid page-header',
        '<main',
    ]
    for m in markers:
        if m in content and m != "<main":
            return content.replace(m, f'<main id="main-content">\n    {m}', 1)
    return content


def close_main_before_footer(content: str) -> str:
    if "</main>" in content:
        return content
    return content.replace(
        "    <footer class=\"sn-footer",
        "    </main>\n\n    <footer class=\"sn-footer",
        1,
    )


for name in PAGES:
    path = ROOT / name
    if not path.exists():
        continue
    text = path.read_text(encoding="utf-8")
    text = replace_head(text)
    text = replace_chrome_top(text)
    text = replace_footer(text)
    text = cleanup_scripts(text, name)
    text = add_main_id(text)
    text = close_main_before_footer(text)
    path.write_text(text, encoding="utf-8")
    print("updated", name)

print("done")
