$(function(){
    $('.tabs').first().show();
    $('.item-nav').first().addClass('item-nav-active');
   
    $('.item-nav').on('click', function(e) {
        e.preventDefault();
        var ref = $(this).attr('href');
		$('.tabs').hide();
		$('.item-nav').removeClass('item-nav-active');
		$(ref).show();
		$(this).addClass('item-nav-active');
    });
})

