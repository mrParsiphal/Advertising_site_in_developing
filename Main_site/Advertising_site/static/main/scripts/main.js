$(function(){
    const list = document.querySelectorAll('.list');
    function activeLink(){
        list.forEach((item) =>
        item.classList.remove('active'));
        this.classList.add('active');
    }
    list.forEach((item) => 
    item.addEventListener('click',activeLink));

    $(document).ready(function() {
        $('.menu-burger__header').click(function() {
            $('.menu-burger__header').toggleClass('open-menu');
            $('.men').toggleClass('open-old-menu');
        });
    });

    var owl = $('.owl-carousel');
owl.owlCarousel({
    loop:false,
    nav:false,   
    margin:30,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },            
        960:{
            items:2
        },
        1200:{
            items:4
        }
    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY>0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});


});    