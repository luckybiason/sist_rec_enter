function pesq(btn) {
	$.ajax({
		url : HASH_LIST_AJAX.URL_LIST_AJAX,
		type : 'get',
		cache : false,
		dataType : 'json',
		data : {
			id : btn
		},
		success : function(retorno) {
			$('tr #datalhes' + btn).empty().show('slow').wrapInner(retorno.html);
			$('#plus' + btn).hide();
			$('#minus' + btn).show();
		},
		error : function(jqXHR, textStatus, errorThrown) {
			alert(gettext('Um erro ocorreu.') + errorThrown)
		}
	});
};

function hide(btn) {
	$('tr #datalhes' + btn).hide().empty();
	$('#plus' + btn).show();
	$('#minus' + btn).hide();
};