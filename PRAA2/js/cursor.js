jQuery(function () {
    "use strict"; document.getElementsByTagName("body")[0].addEventListener("mousemove", function (n) { e.style.left = n.clientX + "px", e.style.top = n.clientY + "px" }); var e = document.getElementById("pointer"); jQuery(document).mousemove(function (e) {
        jQuery(".red-bg").on("mouseenter", function () { jQuery('.pointer').addClass("black") }).on("mouseleave", function () { jQuery('.pointer').removeClass("black") })
        jQuery(".pointer-large, .swiper-button-next, .swiper-button-prev, .mfp-arrow-left, .mfp-arrow-right, .home-slider .swiper-pagination-bullet, .button, .sidebar .widget a").on("mouseenter", function () { jQuery('.pointer').addClass("large") }).on("mouseleave", function () { jQuery('.pointer').removeClass("large") })
        jQuery(".xen-textblock a, .xen-textblock h1 a, .xen-textblock h2 a, .xen-textblock h3 a, .xen-textblock h4 a, .xen-textblock h5 a, .xen-textblock h6 a, p a").on("mouseenter", function () { jQuery('.pointer').addClass("large") }).on("mouseleave", function () { jQuery('.pointer').removeClass("large") })
        jQuery(".pointer-small, .testimonials-slider .swiper-pagination-bullet, .portfolio-slider .swiper-pagination-bullet").on("mouseenter", function () { jQuery('.pointer').addClass("small") }).on("mouseleave", function () { jQuery('.pointer').removeClass("small") })
        jQuery(".mfp-img, .pointer-right").on("mouseenter", function () { jQuery('.pointer').addClass("right") }).on("mouseleave", function () { jQuery('.pointer').removeClass("right") })
        jQuery(".pointer-zoom").on("mouseenter", function () { jQuery('.pointer').addClass("zoom") }).on("mouseleave", function () { jQuery('.pointer').removeClass("zoom") })
        jQuery(".pointer-open").on("mouseenter", function () { jQuery('.pointer').addClass("open") }).on("mouseleave", function () { jQuery('.pointer').removeClass("open") })
    })
})