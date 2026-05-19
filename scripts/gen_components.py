#!/usr/bin/env python3
d = "div"
S = {
    "facebook": "https://www.facebook.com/satellitengonoofficiel?mibextid=ZbWKwL",
    "twitter": "https://twitter.com/NgonoSatellite?t=YXgojc7tG9AOPC16dLQSKw&s=09",
    "linkedin": "https://www.linkedin.com/company/satellite-ngono/",
    "youtube": "https://youtube.com/@ngonosatellite",
}

def tag(cls, inner="", close=True):
    o = f'<{d} class="{cls}">' + inner
    if close:
        o += f"</{d}>"
    return o

topbar = (
    tag("sn-topbar d-none d-lg-block", tag("container", tag("sn-topbar__inner", 
        tag("sn-topbar__left",
            '<span class="sn-topbar__item"><i class="fa fa-map-marker-alt"></i> Zone Portuaire - Face Pharmacam, Douala</span>'
            '<span class="sn-topbar__item"><i class="far fa-clock"></i> Lun - Ven : 08H00 - 17H30</span>'
        , close=True) +
        tag("sn-topbar__right",
            '<span class="sn-topbar__item"><i class="fa fa-phone-alt"></i> +237 657 333 381 / 652 714 013</span>'
            + tag("sn-social d-inline-flex gap-1 ms-2",
                f'<a href="{S["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>'
                f'<a href="{S["twitter"]}" target="_blank" rel="noopener" aria-label="Twitter"><i class="fab fa-twitter"></i></a>'
                f'<a href="{S["linkedin"]}" target="_blank" rel="noopener" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>'
                f'<a href="{S["youtube"]}" target="_blank" rel="noopener" aria-label="YouTube"><i class="fab fa-youtube"></i></a>'
            )
        , close=True)
    , close=True), close=True), close=True)
)

navbar = (
    '<header class="sn-header sticky-top">'
    '<nav class="navbar navbar-expand-lg navbar-light">'
    + tag("container",
        '<a href="index.html" class="navbar-brand d-flex align-items-center">'
        '<img id="logo" src="img/logo-sn.png" alt="Satellite Ngono">'
        '<span class="sn-brand-text d-none d-md-inline ms-2">Satellite Ngono<small>Contrôle technique agréé</small></span>'
        '</a>'
        '<button type="button" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-label="Menu">'
        '<span class="navbar-toggler-icon"></span></button>'
        + f'<{d} class="collapse navbar-collapse" id="navbarCollapse">' + tag("navbar-nav ms-auto align-items-lg-center",
            '<a href="index.html" class="nav-item nav-link">Accueil</a>'
            '<a href="service.html" class="nav-item nav-link">Services</a>'
            '<a href="about.html" class="nav-item nav-link">À propos</a>'
            '<a href="tarif.html" class="nav-item nav-link">Tarifs</a>'
            '<a href="controle.html" class="nav-item nav-link">Contrôle technique</a>'
            '<a href="contact.html" class="nav-item nav-link">Contact</a>'
            '<a href="contact.html" class="btn btn-primary btn-cta ms-lg-3">Prendre rendez-vous</a>'
        , close=True) + f'</{d}>'
    , close=True)
    + '</nav></header>'
)

footer = (
    '<footer class="sn-footer footer pt-5 mt-5">'
    + tag("container py-5", tag("row g-5",
        tag("col-lg-4 col-md-6",
            "<h4>Direction générale</h4>"
            '<p class="mb-2"><i class="fa fa-map-marker-alt me-2"></i>Douala, Cameroun</p>'
            '<p class="mb-2"><i class="fa fa-phone-alt me-2"></i>+237 657 333 381</p>'
            '<p class="mb-2"><i class="fa fa-envelope me-2"></i>contact@satellite-ngono.com</p>'
            + tag("d-flex pt-2 gap-2",
                f'<a class="btn btn-outline-light btn-social" href="{S["facebook"]}" target="_blank" rel="noopener"><i class="fab fa-facebook-f"></i></a>'
                f'<a class="btn btn-outline-light btn-social" href="{S["twitter"]}" target="_blank" rel="noopener"><i class="fab fa-twitter"></i></a>'
                f'<a class="btn btn-outline-light btn-social" href="{S["linkedin"]}" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>'
                f'<a class="btn btn-outline-light btn-social" href="{S["youtube"]}" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a>'
            )
        ) +
        tag("col-lg-5 col-md-6",
            "<h4>Horaires d'ouverture</h4>"
            '<h5 class="text-light mb-2">Agence de Yaoundé</h5>'
            '<p class="mb-1">Lun - Ven : 07H30 - 21H00 · Sam : 07H30 - 15H00</p>'
            '<h5 class="text-light mb-2 mt-3">Agence de Douala</h5>'
            '<p class="mb-1">Lun - Ven : 07H30 - 20H00 · Sam : 07H30 - 15H00</p>'
            '<h5 class="text-light mb-2 mt-3">Agence de Garoua</h5>'
            '<p class="mb-1">Lun - Ven : 07H30 - 17H00 · Sam : 07H30 - 15H00</p>'
            '<h5 class="text-light mb-2 mt-3">Agence de Bafoussam</h5>'
            '<p class="mb-0">Lun - Ven : 07H30 - 17H00 · Sam : 07H30 - 15H00</p>'
        ) +
        tag("col-lg-3 col-md-6",
            "<h4>Newsletter</h4>"
            "<p>Retrouvez toutes les informations nous concernant ici!</p>"
            + tag("position-relative", '<input class="form-control border-0 w-100 py-3 ps-4 pe-5" type="email" placeholder="Votre email" aria-label="Email">'
            '<button type="button" class="btn btn-primary py-2 position-absolute top-0 end-0 mt-2 me-2">Envoyer</button>')
        )
    ))
    + tag("container", tag("copyright", tag("row",
        tag("col-md-12 text-center",
            '&copy; <a href="index.html">SATELLITE NGONO</a>, Tous droits réservés. · '
            '<a href="https://agency.talk-adk.com" target="_blank" rel="noopener">COMMUNITECH &amp; SOLUTIONS</a>'
        )
    )))
    + '</footer>'
)

js = f'''/**
 * Shared chrome for pages with #topbar, #navbar, #footer placeholders.
 */
(function () {{
    "use strict";

    function inject(selector, html) {{
        var el = document.querySelector(selector);
        if (el) {{
            el.insertAdjacentHTML("afterbegin", html);
        }}
    }}

    function setActiveNav() {{
        var page = window.location.pathname.split("/").pop() || "index.html";
        document.querySelectorAll(".sn-header .nav-link").forEach(function (link) {{
            var href = link.getAttribute("href");
            if (href === page || (page === "" && href === "index.html")) {{
                link.classList.add("active");
            }}
        }});
    }}

    var topbarHtml = {topbar!r};
    var navbarHtml = {navbar!r};
    var footerHtml = {footer!r};

    inject("#topbar", topbarHtml);
    inject("#navbar", navbarHtml);
    inject("#footer", footerHtml);
    setActiveNav();
}})();
'''

with open("/Users/admin/satellite-ngono/js/components.js", "w", encoding="utf-8") as f:
    f.write(js)
print("OK", len(js))
