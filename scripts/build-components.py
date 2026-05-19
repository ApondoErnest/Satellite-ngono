#!/usr/bin/env python3
"""Generate js/components.js"""

COMPONENTS = '''/**
 * Shared chrome for pages with #topbar, #navbar, #footer placeholders.
 */
(function () {
    "use strict";

    var SOCIAL = {
        facebook: "https://www.facebook.com/satellitengonoofficiel?mibextid=ZbWKwL",
        twitter: "https://twitter.com/NgonoSatellite?t=YXgojc7tG9AOPC16dLQSKw&s=09",
        linkedin: "https://www.linkedin.com/company/satellite-ngono/",
        youtube: "https://youtube.com/@ngonosatellite"
    };

    function inject(selector, html) {
        var el = document.querySelector(selector);
        if (el) {
            el.insertAdjacentHTML("afterbegin", html);
        }
    }

    function setActiveNav() {
        var page = window.location.pathname.split("/").pop() || "index.html";
        document.querySelectorAll(".sn-header .nav-link").forEach(function (link) {
            var href = link.getAttribute("href");
            if (href === page || (page === "" && href === "index.html")) {
                link.classList.add("active");
            }
        });
    }

    var topbarHtml =
        '<div class="sn-topbar d-none d-lg-block">' +
        '<div class="container">';

    var navbarHtml = "";

    var footerHtml = "";

    inject("#topbar", topbarHtml);
    inject("#navbar", navbarHtml);
    inject("#footer", footerHtml);
    setActiveNav();
})();
'''

# Fix motion -> div in generated broken placeholder
COMPONENTS = COMPONENTS.replace("<div", "<div").replace("<div", "<div").replace("</div>", "</div>")

with open("/Users/admin/satellite-ngono/js/components.js", "w", encoding="utf-8") as f:
    f.write(COMPONENTS)
