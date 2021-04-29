$(document).ready(function () {
    $('.tooltipped').tooltip({
        'inDuration': 300,
        'transitionMovement': 5,
        'exitDelay': 0,
    });
});


AOS.init({
    duration: 800,
    easing: 'slide',
    once: true
});