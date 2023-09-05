
var owl = $('.owl-carousel');
owl.owlCarousel({
    margin: 25,
    loop: true,
    dots: false,
    nav: true,
    autoplay: true,
    autoplayTimeout: 5000,
    smartSpeed: 4000,
    responsive: {
        0: {
            items: 2
        },

        600: {
            items: 2
        },
        767: {
            items: 3
        },
        1000: {
            items: 4
        }
    }
})
