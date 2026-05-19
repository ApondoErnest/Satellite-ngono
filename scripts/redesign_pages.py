#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("/Users/admin/satellite-ngono")
AGENCIES = (ROOT / "partials/index-agencies.html").read_text(encoding="utf-8")
SERVICES = (ROOT / "partials/index-services-grid.html").read_text(encoding="utf-8")

HERO = """                                    <p class="sn-section-label text-white mb-2">Centre agréé depuis 2006</p>
                                    <h1 class="display-4 text-white mb-4">Votre centre agréé de contrôle technique</h1>
                                    <p class="mb-4" style="color: rgba(255,255,255,0.85);">Sécurité routière et homologation à Douala, Yaoundé, Garoua et Bafoussam.</p>
                                    <div class="btn-group-hero">
                                        <a href="tarif.html" class="btn btn-primary py-3 px-4">Voir les tarifs</a>
                                        <a href="contact.html" class="btn btn-outline-light py-3 px-4">Nous contacter</a>
                                    </motion>""".replace("</motion>", "</div>")

OLD_CAPTION = """                                    <h6 class="text-white text-uppercase mb-3 animated slideInDown">// Satellite Ngono //</h6>
                                    <h1 class="display-3 text-white mb-4 pb-3 animated slideInDown">Votre centre agréé de contrôle technique</h1>
                                    <a href="about.html" class="btn btn-primary py-3 px-5 animated slideInDown">Voir plus<i class="fa fa-arrow-right ms-3"></i></a>"""


def patch_index():
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace('class="container-fluid p-0 mb-5"', 'class="container-fluid p-0 sn-hero"', 1)
    text = text.replace('data-bs-ride="carousel"', 'data-bs-ride="carousel" data-bs-interval="8000"', 1)
    text = text.replace(OLD_CAPTION, HERO)
    text = re.sub(r"<!-- Agency Start -->.*?<!-- Agency End -->", AGENCIES.strip(), text, flags=re.DOTALL)
    text = re.sub(r"<!-- Service Start -->.*?<!-- Service End -->", SERVICES.strip(), text, flags=re.DOTALL)
    text = text.replace("// A Propos //", "À propos")
    text = text.replace('style="background: rgba(0, 0, 0, .08);"', 'class="sn-experience-badge"')
    text = text.replace(
        'class="container-fluid fact bg-dark my-5 py-5 chiffre"',
        'class="container-fluid fact sn-stats my-5 py-5 chiffre"',
    )
    text = re.sub(
        r'(<h2 class="text-white mb-2" data-toggle="counter-up">)3(</h2>\s*<p class="text-white mb-0">Centres fixes)',
        r"\g<1>4\2",
        text,
    )
    text = text.replace("// Notre équipe //", "Notre équipe")
    text = text.replace("// Nos clients //", "Nos clients")
    text = re.sub(r"\n    <!-- Back to Top -->.*?</a>\n", "\n", text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")
    print("index ok")


def patch_empty(name, title, crumb):
    path = ROOT / name
    text = path.read_text(encoding="utf-8")
    inner = f"""    <main id="main-content">
    <section class="sn-section">
        <div class="container-fluid page-header mb-5 sn-page-hero" style="background-image: url('img/carousel-bg-1.jpg');">
            <div class="container">
                <div class="page-header-inner py-5">
                    <motion class="container text-center">
                        <h1 class="display-5 text-white">{title}</h1>
                        <nav aria-label="Fil d'Ariane"><ol class="breadcrumb justify-content-center mb-0"><li class="breadcrumb-item"><a href="index.html">Accueil</a></li><li class="breadcrumb-item active text-white" aria-current="page">{crumb}</li></ol></nav>
                    </div>
                </div>
            </div>
        </div>
        <div class="container sn-empty-state py-5">
            <i class="fa fa-clock" aria-hidden="true"></i>
            <h2>Bientôt disponible</h2>
            <p>Cette section sera publiée prochainement.</p>
            <a href="contact.html" class="btn btn-primary mt-3">Nous contacter</a>
        </div>
    </section>
    </main>"""
    inner = inner.replace("<motion", "<div").replace("</motion>", "</div>")
    text = re.sub(r"\s*<main id=\"main-content\">\s*</main>", "\n" + inner, text, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")
    print(name, "ok")


def patch_contact():
    path = ROOT / "contact.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("danas les", "dans les")
    text = text.replace('class="text-uppercase">// Yaoundé //', 'class="sn-section-label">Yaoundé')
    text = text.replace('class="text-uppercase">// Douala //', 'class="sn-section-label">Douala')
    text = text.replace('class="text-uppercase">// Garoua //', 'class="sn-section-label">Garoua')
    text = re.sub(
        r'<iframe([^>]*)\s+width="415"\s+height="200"([^>]*)>',
        r'<div class="sn-map-wrap"><iframe\1\2>',
        text,
    )
    text = text.replace("</iframe>", "</iframe></div>")
    text = re.sub(r'<div class="sn-map-wrap"><div class="sn-map-wrap">', '<div class="sn-map-wrap">', text)
    text = text.replace(
        '<div class=" wow fadeInUp" data-wow-delay="0.2s">',
        '<div class="sn-contact-form wow fadeInUp" data-wow-delay="0.2s">',
    )
    path.write_text(text, encoding="utf-8")
    print("contact ok")


def patch_404():
    path = ROOT / "404.html"
    text = path.read_text(encoding="utf-8")
    if "sn-404" not in text:
        text = re.sub(
            r"(<main id=\"main-content\">.*?<!-- Page Header End -->)",
            r"\1\n    <section class=\"sn-section sn-404\"><div class=\"container text-center py-5\"><i class=\"bi bi-exclamation-triangle\"></i><h1 class=\"mb-3\">Page introuvable</h1><p class=\"text-muted mb-4\">La page demandée n'existe pas ou a été déplacée.</p><a href=\"index.html\" class=\"btn btn-primary\">Retour à l'accueil</a></div></section>",
            text,
            flags=re.DOTALL,
            count=1,
        )
    path.write_text(text, encoding="utf-8")
    print("404 ok")


if __name__ == "__main__":
    patch_index()
    patch_empty("actualite.html", "Actualités", "Actualités")
    patch_empty("rejoindre.html", "Nous rejoindre", "Carrières")
    patch_contact()
    patch_404()
