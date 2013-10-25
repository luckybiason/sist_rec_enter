var carousel = carousel || {};

createTv = function(listJson, elem){
	var data = listJson;
	var localDefault = elem +' .tv';
	var localDefaultB = elem +' .bullets';
	
	$.each(data, function(i) {
		var itemTv = '<div class="item-tv item-'+i+'">';
			itemTv += '<figure>';
			itemTv +='<a href="'+ data[i].url + '" title="" >';
			itemTv +='<img src="'+ data[i].img+ '" alt="" />';
			itemTv +='</a>';
			itemTv +='</figure>';
			itemTv +='</div>';
			bullet = '<a href="#" title="" class="bullet" data-ref="item-'+i+'"></a>';
			$(localDefault).append(itemTv);
			$(localDefaultB).append(bullet);
	})
	functionalityTv(elem);
}
functionalityTv = function(elem){
	$('.item-tv', elem).first().show();
	$('.bullet', elem).first().addClass('bullet-actived');
	
	$('.bullet', elem).live('click', function(e){
		e.preventDefault();
		var refBullet = '.'+$(this).attr('data-ref');
		$('.bullet', elem).removeClass('bullet-actived');
		$(this).addClass('bullet-actived');
		$('.item-tv', elem).hide();
		$(refBullet, elem).fadeIn('slide');
	});
}