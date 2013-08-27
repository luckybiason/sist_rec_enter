var setupRaty = function() {
	$.fn.raty.defaults.path = IMG_RATY;
	$('#comnts_rat').raty({
		halfShow : false,
		score    : 3,
		click    : function(score, evt) {
			$('#comnts_nota').val(score);
		}
	});
}

$(function() {
	setupRaty();
	
	
	$('#comnts_submit').click(function(){
        $.ajax({
            url     : URL_COMNT_SAVE,
            type    : 'get',
            dataType: 'json',
            data: {
                id_televisor : ID_TELEVISOR,
                nome         : $('#comnts_nome').val(),
                comentario   : $('#comnts_comentario').val(),
                nota         : $('#comnts_nota').val()
            },
			success: function(retorno){
				/*$('#tbl_listagem').empty().wrapInner(retorno.html);
				$('#mensage').empty().wrapInner(retorno.qtd+' registros encontrados.')
				criarTabela('tbl_listagem','toGroupFilter')*/
			},
			error: function(jqXHR, textStatus, errorThrown){
				alert('Um erro ocorreu. - '+errorThrown)
			}
	    });
    });

});
