/**
 * Satellite Ngono UI helpers (design layer only)
 */
(function () {
    "use strict";

    document.addEventListener("DOMContentLoaded", function () {
        document.body.classList.add("sn-loaded");

        var page = window.location.pathname.split("/").pop() || "index.html";
        document.querySelectorAll("[data-nav]").forEach(function (link) {
            if (link.getAttribute("data-nav") === page) {
                link.classList.add("active");
            }
        });

        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
            document.querySelectorAll(".wow").forEach(function (el) {
                el.classList.remove("wow");
            });
        }
    });
})();
