var carousel = carousel || {};
var create = function(listJson, elem){
	var data = listJson;
	var localDefault = elem +' .offersCarr';
	$.each(data, function(i) {
		var itemCarr = '<div class="item-carousel offer-block">';
			itemCarr +='<a href="'+ data[i].url + '" title="" class="link-box-offer">';
			itemCarr +=' <span class="item1">';
			itemCarr +='<figure>';
			itemCarr +='<img src="'+ data[i].img+ '" alt="" />';
			itemCarr +='</figure>';
			itemCarr +='<p class="description txt-box-offer">'+ data[i].descricao + '</p>';
			itemCarr +='<p class="aux txt-box-offer">'+ data[i].aux +'</p>';
			itemCarr +='</span>';
			itemCarr +='</a>';
			itemCarr +='</div>';
			$(localDefault).append(itemCarr);
			
	});
	functionality(elem);
	
}

var functionality  = function(elem){
	var
	voltar = $('.prev', elem),
	avancar = $('.next', elem),
	num_pages = Math.ceil($('.offer-block', elem).size() / 3),
	curr_page = 1,
	step = $('#imgsOffers', elem).width(),
	velocidade = 450;
	if($('.offer-block', elem).size() <= 3){
		voltar.hide(); avancar.hide();
	}
	if(curr_page == 1){
	    $('.prev', elem).hide();
	}
	$('.offer-block', elem).first().addClass('first');
	$('.offer-block', elem).last().addClass('last');
	$('.offersCarr', elem).css('width', num_pages * step)
	
	var click_action = function(action, ref){
	
		if(action == 'prev'){
			curr_page--;
		}
		if(action == 'next'){
			curr_page++;
		}
		var pos = -(curr_page - 1) * step;
		if(curr_page == 1 ){
			voltar.hide();
		}else{
			voltar.show();
		}
		if(curr_page == num_pages){
			avancar.hide();
		}else{
			avancar.show();
		}
		var carr = '.offersCarr';
		$(carr, elem).animate({'left': pos + 'px'}, velocidade);
	};
	avancar.click(function(e){
		e.preventDefault();
		click_action('next', elem);
	});
	voltar.click(function(e){
		e.preventDefault();
		click_action('prev',elem);
	});
}