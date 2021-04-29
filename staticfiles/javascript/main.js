AOS.init({
    duration: 800,
    easing: 'slide',
    once: true
});

$('.js-clone-nav').each(function () {
    var $this = $(this);
    $this.clone().attr('class', 'site-nav-wrap').appendTo('.site-mobile-menu-body');
});

