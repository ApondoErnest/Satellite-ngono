/**
 * Home page — inline service detail panel
 */
(function () {
    "use strict";

    document.addEventListener("DOMContentLoaded", function () {
        var picker = document.querySelector(".sn-home-services");
        if (!picker) return;

        var buttons = picker.querySelectorAll(".sn-service-picker__btn");
        var panels = picker.querySelectorAll(".sn-service-detail");

        function showService(id) {
            buttons.forEach(function (btn) {
                var active = btn.getAttribute("data-service") === id;
                btn.classList.toggle("active", active);
                btn.setAttribute("aria-expanded", active ? "true" : "false");
            });
            panels.forEach(function (panel) {
                var active = panel.id === "detail-" + id;
                panel.classList.toggle("active", active);
                panel.hidden = !active;
            });
        }

        buttons.forEach(function (btn) {
            btn.addEventListener("click", function () {
                showService(btn.getAttribute("data-service"));
            });
        });

        if (buttons.length) {
            showService(buttons[0].getAttribute("data-service"));
        }
    });
})();
