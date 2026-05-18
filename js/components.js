/*Topbar Start*/

var topbarComponent = "<!-- Topbar Start -->\n" +
    "\n" +
    "<div id=\"topbar\" class=\"container-fluid bg-light p-0\">\n" +
    "    <div class=\"row gx-0 d-none d-lg-flex\">\n" +
    "        <div class=\"col-lg-7 px-5 text-start\">\n" +
    "            <div class=\"h-100 d-inline-flex align-items-center py-3 me-4\">\n" +
    "                <small class=\"fa fa-map-marker-alt text-primary me-2\"></small>\n" +
    "                <small>Direction Générale : Zone Portuaire - Face Pharmacam, Douala, Cameroun</small>\n" +
    "            </div>\n" +
    "            <div class=\"h-100 d-inline-flex align-items-center py-3\">\n" +
    "                <small class=\"far fa-clock text-primary me-2\"></small>\n" +
    "                <small>Lun - Ven : 08H00 - 17H30</small>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"col-lg-5 px-5 text-end\">\n" +
    "            <div class=\"h-100 d-inline-flex align-items-center py-3 me-4\">\n" +
    "                <small class=\"fa fa-phone-alt text-primary me-2\"></small>\n" +
    "                <small>+237 657 333 381</small>\n" +
    "            </div>\n" +
    "            <div class=\"h-100 d-inline-flex align-items-center\">\n" +
    "                <a class=\"btn btn-sm-square bg-white text-primary me-1\" href=\"\"><i class=\"fab fa-facebook-f\"></i></a>\n" +
    "                <a class=\"btn btn-sm-square bg-white text-primary me-1\" href=\"\"><i class=\"fab fa-twitter\"></i></a>\n" +
    "                <a class=\"btn btn-sm-square bg-white text-primary me-1\" href=\"\"><i class=\"fab fa-linkedin-in\"></i></a>\n" +
    "                <a class=\"btn btn-sm-square bg-white text-primary me-0\" href=\"\"><i class=\"fab fa-instagram\"></i></a>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "    </div>\n" +
    "</div>\n" +
    "<!-- Topbar End -->"
var topbar = document.querySelector("#topbar");
topbar.insertAdjacentHTML("afterbegin",topbarComponent);

/* Topbar End */

/* Navbar Star */

var navbarComponent = "    <!-- Navbar Start -->\n" +
    "    <nav class=\"navbar navbar-expand-lg bg-white navbar-light shadow sticky-top p-0\">\n" +
    "        <a href=\"index.html\" class=\"navbar-brand d-flex align-items-center px-4 px-lg-5\">\n" +
    "           <img id='logo' src=\"../img/logo-sn.jpeg\" class=\"img-fluid\" alt=\"logo\">\n" +
    /*"            <h2 class=\"m-0 text-primary\"><i class=\"fa fa-car me-3\"></i>CarServ</h2>\n" +*/
    "        </a>\n" +
    "        <button type=\"button\" class=\"navbar-toggler me-4\" data-bs-toggle=\"collapse\" data-bs-target=\"#navbarCollapse\">\n" +
    "            <span class=\"navbar-toggler-icon\"></span>\n" +
    "        </button>\n" +
    "        <div class=\"collapse navbar-collapse\" id=\"navbarCollapse\">\n" +
    "            <div class=\"navbar-nav ms-auto p-4 p-lg-0\">\n" +
    "                <a href=\"index.html\" class=\"nav-item nav-link\">Accueil</a>\n" +
    "                <a href=\"controle.html\" class=\"nav-item nav-link\">Contrôle Technique</a>\n" +
    "                <a href=\"service.html\" class=\"nav-item nav-link\">Services</a>\n" +
    "                <a href=\"tarif.html\" class=\"nav-item nav-link\">Tarifs</a>\n" +
    "                <a href=\"about.html\" class=\"nav-item nav-link\">A Propos</a>\n" +
    "                <a href=\"rejoindre.html\" class=\"nav-item nav-link\">Nous rejoindre</a>\n" +
    "                <a href=\"actualite.html\" class=\"nav-item nav-link\">Actualités</a>\n" +
    "                <div class=\"nav-item dropdown\">\n" +
    "                    <a href=\"#\" class=\"nav-link dropdown-toggle\" data-bs-toggle=\"dropdown\">Pages</a>\n" +
    "                    <div class=\"dropdown-menu fade-up m-0\">\n" +
    "                        <a href=\"booking.html\" class=\"dropdown-item\">Booking</a>\n" +
    "                        <a href=\"team.html\" class=\"dropdown-item\">Technicians</a>\n" +
    "                        <a href=\"testimonial.html\" class=\"dropdown-item\">Testimonial</a>\n" +
    "                        <a href=\"404.html\" class=\"dropdown-item\">404 Page</a>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "                <a href=\"contact.html\" class=\"nav-item nav-link\">Contact</a>\n" +
    "            </div>\n" +
    "            <a href=\"\" class=\"btn btn-primary py-4 px-lg-5 d-none d-lg-block\">Get A Quote<i class=\"fa fa-arrow-right ms-3\"></i></a>\n" +
    "        </div>\n" +
    "    </nav>\n" +
    "    <!-- Navbar End -->"
var navbar = document.querySelector("#navbar");
navbar.insertAdjacentHTML("afterbegin", navbarComponent);
link=document.querySelectorAll(".nav-item")
link.onclick=function (){
 alert(link.text);
}
/* Navbar End */

/* Footer start */
var footerComponent = "" +
    "<!-- Footer Start -->\n" +
    "    <div class=\"container-fluid bg-dark text-light footer pt-5 mt-5 wow fadeIn\" data-wow-delay=\"0.1s\">\n" +
    "        <div class=\"container py-5\">\n" +
    "            <div class=\"row g-5\">\n" +
    "                <div class=\"col-lg-3 col-md-6\">\n" +
    "                    <h4 class=\"text-light mb-4\">Adresse</h4>\n" +
    "                    <p class=\"mb-2\"><i class=\"fa fa-map-marker-alt me-3\"></i>Zone Portuaire - Face Pharmacam, Douala, Cameroun</p>\n" +
    "                    <p class=\"mb-2\"><i class=\"fa fa-phone-alt me-3\"></i>+237 657 333 381</p>\n" +
    "                    <p class=\"mb-2\"><i class=\"fa fa-envelope me-3\"></i>contact@satellite-ngono.com</p>\n" +
    "                    <div class=\"d-flex pt-2\">\n" +
    "                        <a class=\"btn btn-outline-light btn-social\" href=\"\"><i class=\"fab fa-twitter\"></i></a>\n" +
    "                        <a class=\"btn btn-outline-light btn-social\" href=\"\"><i class=\"fab fa-facebook-f\"></i></a>\n" +
    "                        <a class=\"btn btn-outline-light btn-social\" href=\"\"><i class=\"fab fa-youtube\"></i></a>\n" +
    "                        <a class=\"btn btn-outline-light btn-social\" href=\"\"><i class=\"fab fa-linkedin-in\"></i></a>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "                <div class=\"col-lg-3 col-md-6\">\n" +
    "                    <h4 class=\"text-light mb-4\">Horaires d'ouverture</h4>\n" +
    "                    <h6 class=\"text-light\">Lundi - Vendredi:</h6>\n" +
    "                    <p class=\"mb-4\">08H00 - 17H30</p>\n" +
    "                    <h6 class=\"text-light\">Samedi:</h6>\n" +
    "                    <p class=\"mb-0\">08H00 - 12H00</p>\n" +
    "                </div>\n" +
    "                <div class=\"col-lg-3 col-md-6\">\n" +
    "                    <h4 class=\"text-light mb-4\">Services</h4>\n" +
    "                    <a class=\"btn btn-link\" href=\"\">Diagnostic Test</a>\n" +
    "                    <a class=\"btn btn-link\" href=\"\">Engine Servicing</a>\n" +
    "                    <a class=\"btn btn-link\" href=\"\">Tires Replacement</a>\n" +
    "                    <a class=\"btn btn-link\" href=\"\">Oil Changing</a>\n" +
    "                    <a class=\"btn btn-link\" href=\"\">Vacuam Cleaning</a>\n" +
    "                </div>\n" +
    "                <div class=\"col-lg-3 col-md-6\">\n" +
    "                    <h4 class=\"text-light mb-4\">Newsletter</h4>\n" +
    "                    <p>Retrouvez toutes les informations nous concernant ici!</p>\n" +
    "                    <div class=\"position-relative mx-auto\" style=\"max-width: 400px;\">\n" +
    "                        <input class=\"form-control border-0 w-100 py-3 ps-4 pe-5\" type=\"text\" placeholder=\"Votre email\">\n" +
    "                        <button type=\"button\" class=\"btn btn-primary py-2 position-absolute top-0 end-0 mt-2 me-2\">Envoyer</button>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"container\">\n" +
    "            <div class=\"copyright\">\n" +
    "                <div class=\"row\">\n" +
    "                    <div class=\"col-md-6 text-center text-md-start mb-3 mb-md-0\">\n" +
    "                        &copy; <a class=\"border-bottom\" href=\"#\">SATELLITE NGONO</a>, All Right Reserved.\n" +
    "\n" +
    "                        <!--/*** This template is free as long as you keep the footer author’s credit link/attribution link/backlink. If you'd like to use the template without the footer author’s credit link/attribution link/backlink, you can purchase the Credit Removal License from \"https://htmlcodex.com/credit-removal\". Thank you for your support. ***/-->\n" +
    "                        Designed By <a class=\"border-bottom\" href=\"https://agency.talk-adk.com\">TALK-ADK</a>\n" +
    "                    </div>\n" +
    "                    <div class=\"col-md-6 text-center text-md-end\">\n" +
    "                        <div class=\"footer-menu\">\n" +
    "                            <a href=\"\">Accueil</a>\n" +
    "                            <a href=\"\">Cookies</a>\n" +
    "                            <a href=\"\">Help</a>\n" +
    "                            <a href=\"\">FQAs</a>\n" +
    "                        </div>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "    </div>\n" +
    "    <!-- Footer End -->"
var footer = document.querySelector("#footer");
footer.insertAdjacentHTML("afterbegin", footerComponent);

// Get the logoID /
/*
var logo = document.querySelector(".logo");
logo.setAttribute("id","logo");
*/