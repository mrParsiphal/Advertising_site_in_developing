$(function(){
	$('.owl-carousel').owlCarousel({
	    loop:true,
	    margin:30,
	    nav:false,
	    responsive:{
	        0:{
	            items:1
	        },
	        600:{
	            items:2
	        },
	        1000:{
	            items:4
	        }
	    }
	});	

		var owl = $('.owl-carousel');
	owl.owlCarousel({
	    loop:true,
	    nav:true,
	    margin:10,
	    responsive:{
	        0:{
	            items:1
	        },
	        600:{
	            items:3
	        },            
	        960:{
	            items:5
	        },
	        1200:{
	            items:6
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


	$('.mv_block1').click(function() {
        $('.music_vdeo').replaceWith('<div class="col-lg-6 music_vdeo">					<iframe width="560" height="315" src="https://www.youtube.com/embed/Qp078LJhFI8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>				</div>');
    });

    $('.mv_block2').click(function() {
        $('.music_vdeo').replaceWith('<div class="col-lg-6 music_vdeo">					<iframe width="560" height="315" src="https://www.youtube.com/embed/3iZ2DfKpWhE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>				</div>');
    });

    $('.mv_block3').click(function() {
        $('.music_vdeo').replaceWith('<div class="col-lg-6 music_vdeo">					<iframe width="560" height="315" src="https://www.youtube.com/embed/p7CudbgVJT4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>				</div>');
    });

    $('.mv_block4').click(function() {
        $('.music_vdeo').replaceWith('<div class="col-lg-6 music_vdeo">					<iframe width="560" height="315" src="https://www.youtube.com/embed/pfuzVWWsgoA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>				</div>');
    });

    $('.mv_block5').click(function() {
        $('.music_vdeo').replaceWith('<div class="col-lg-6 music_vdeo">					<iframe width="560" height="315" src="https://www.youtube.com/embed/uZ8PHB-06xg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>				</div>');
    });

// **************************************************************************
// **************************************************************************
// **************************************************************************






});