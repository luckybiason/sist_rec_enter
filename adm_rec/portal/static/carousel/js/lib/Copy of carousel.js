var carousel = carousel || {};

create = function(listJson, elem){
	var data = listJson;
	var localDefault = elem;
	//$(localDefault).addClass('carousel');
	var html = '<div class="carousel">';
	html += '<div href="#" class="prev-box"> <a href="#" alt="voltar" class="prev"> </a> </div>';
	html += '<div class="carousel" id="imgsOffers"><div class="carr offersCarr">';
	$.each(data, function(i) {
		var itemCarr = '<div class="item-carousel offer-block">';
			itemCarr +=     '<a href="'+ data[i].url + '" title="" class="link-box-offer">';
			itemCarr +=       ' <span class="item1">';
			itemCarr +=           '<img src="'+ data[i].img+ '" alt="" width="110px" height="80px" class="car_img"/>';
			itemCarr +=           '<p class="description txt-box-offer">'+ data[i].descricao + '</p>';
			itemCarr +=           '<p class="aux-txt-box-offer">'+ data[i].aux +'</p>';
			itemCarr +=        '</span>';
			itemCarr +=     '</a>';
			itemCarr +='</div>';
			html += itemCarr;
	})
	html += '</div></div>';
	html += '<div href="#" class="next-box"> <a href="#" alt="avançar" class="next"> </a> </div>';
	html += '</div>';
	$(localDefault).html(html);
}

/*INI: CARROSSEL*/
functionality  = function(elem, pai){
	var
	voltar = $('.prev'),
	avancar = $('.next'),
	num_pages = Math.ceil($('.offer-block').size() / 3),
	curr_page = 1,
	step = $('#imgsOffers').width(),
	velocidade = 450;
	if($('.offer-block').size() <= 3){
		voltar.hide(); avancar.hide();
	}
	if(curr_page == 1){
	    $('.prev').hide();
	}
	$('.offer-block').first().addClass('first');
	$('.offer-block').last().addClass('last');
	$('.offersCarr').css('width', num_pages * step)

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
		var carr = ref + ' .offersCarr';
		$(carr).animate({'left': pos + 'px'}, velocidade);
	};
	avancar.click(function(e){
		e.preventDefault();
		var x = '#'+$(this).parent().parent().attr('id');
		click_action('next', x);
	});
	voltar.click(function(e){
		e.preventDefault();
		var x = '#'+$(this).parent().parent().attr('id');
		click_action('prev',x);
	});
}
/*END: Carrossel */