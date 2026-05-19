#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("/Users/admin/satellite-ngono")

def add_script(path, before="</body>"):
    text = path.read_text(encoding="utf-8")
    if "sn-ui.js" not in text:
        text = text.replace(before, '    <script src="js/sn-ui.js"></script>\n' + before)
    path.write_text(text, encoding="utf-8")


def patch_controle():
    p = ROOT / "controle.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
    t = re.sub(r"// (\w+) //", lambda m: m.group(1).capitalize(), t)
    t = re.sub(r'class="text-primary text-uppercase">(\w+)', r'class="sn-section-label">\1', t)
    t = t.replace('<motion class="roadworthiness">', '<div class="roadworthiness container">').replace("<motion", "<div")
    t = t.replace('motion>', 'div>')
    t = t.replace('<div class="container">', '<div class="container-xxl sn-section"><div class="container">', 1)
    p.write_text(t, encoding="utf-8")
    print("controle")


def patch_tarif():
    p = ROOT / "tarif.html"
    t = p.read_text(encoding="utf-8")
    if "<title>Tarifs" not in t:
        t = re.sub(r"<title>.*?</title>", "<title>Tarifs - Satellite Ngono</title>", t, count=1)
    t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
    t = t.replace('class="d-flex py-5 px-4"', 'class="sn-card sn-price-card d-flex flex-column align-items-center text-center p-4 h-100"')
    t = t.replace('class="d-flex py-1 px-4"', 'class="sn-card sn-price-card d-flex flex-column align-items-center text-center p-4 h-100"')
    t = re.sub(r"<p>Prix : ([^<]+)</p>", r'<p class="sn-price">\1</p>', t)
    t = re.sub(r"<p>Validité : ([^<]+)</p>", r'<span class="sn-badge">\1</span>', t)
    t = t.replace("<!-- Catégories start -->", '<section class="sn-section sn-tarif-grid"><div class="container">')
    p.write_text(t, encoding="utf-8")
    print("tarif")


def patch_service():
    p = ROOT / "service.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
    t = t.replace('class="nav w-100 nav-pills me-4"', 'class="nav w-100 nav-pills me-4 sn-service-nav"')
    t = t.replace("// Le Contrôle Technique //", "Contrôle technique")
    p.write_text(t, encoding="utf-8")
    print("service")


def patch_about():
    p = ROOT / "about.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
    t = re.sub(r"// ([^/]+) //", lambda m: m.group(1).strip(), t)
    p.write_text(t, encoding="utf-8")
    print("about")


def patch_contact():
    p = ROOT / "contact.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
    p.write_text(t, encoding="utf-8")


def patch_booking_team():
    for name in ("booking.html", "team.html", "testimonial.html"):
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        t = t.replace('class="container-fluid page-header', 'class="container-fluid page-header sn-page-hero')
        t = re.sub(r"<title>CarServ[^<]*</title>", f"<title>{name.replace('.html','').title()} - Satellite Ngono</title>", t, flags=re.I)
        if name == "team.html":
            t = re.sub(r"<h5 class=\"fw-bold mb-0\">Full Name</h5>", "", t)
        p.write_text(t, encoding="utf-8")
        print(name)


if __name__ == "__main__":
    patch_controle()
    patch_tarif()
    patch_service()
    patch_about()
    patch_contact()
    patch_booking_team()
    for html in ROOT.glob("*.html"):
        add_script(html)
