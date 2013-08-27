/* Faz a configuração das estrelas de notas no cadastro de comentários */
var setupRaty = function() {
	$.fn.raty.defaults.path = IMG_RATY;
	$('#comnts_rat').raty({
		halfShow : false,
		score    : 3,
		click    : function(score, evt) {
			$('#comnts_nota').val(score); // altera o valor do campo de nota do formulário
		}
	});
}

/* Faz a configuração das estrelas de notas na listagem de comentários */
var setupRatyID = function(id, score) {
	$.fn.raty.defaults.path = IMG_RATY;
	$('#'+id).raty({
		halfShow : false,
		score    : score,
		readOnly : true,
	});
}

/* Carrega e monta os comentários cadastrados para o televisor */
var carrega_lista = function(){
	 $.ajax({
            url     : URL_COMNT_LIST,
            type    : 'get',
            dataType: 'json',
            data: {
                id_televisor : ID_TELEVISOR
            },
			success: function(retorno){
				var coments = retorno.coments;
				$('#lista_comentarios').empty();
				$.each(coments, function(index,coment){
					var html = '<div class="coment">';
					html += '<p class="data-coment"><strong>Data: ' + coment.data + '</strong></p>';
					html += '<p class="name-coment"><strong>Nome: ' + coment.nome + '</strong></p>';
					html += '<p class="rati-coment"><span id="comnts_rati_' + coment.id + '"><!-- --></span></p>';
					html += '<p class="txt-coment parag-default">' + coment.comentario + '</p>';
					html += '</div>';
				    $('#lista_comentarios').append(html);
				    setupRatyID("comnts_rati_"+ coment.id,coment.nota);
                });
			},
			error: function(jqXHR, textStatus, errorThrown){
				alert('Um erro ocorreu. - '+errorThrown)
			}
	    });
}

/* Cadastra o comentário */
var cadastrar_comentario = function(){
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
				if (retorno.erro){
					jError(retorno.erro,config ); 
				}else{
					jSuccess(retorno.status,config );
				    carrega_lista();
					// Limpa campos
	                $('#comnts_nome').val(''),
	                $('#comnts_comentario').val(''),
	                $('#comnts_nota').val('')
				}
			},
			error: function(jqXHR, textStatus, errorThrown){
				alert('Um erro ocorreu. - '+errorThrown)
			}
	    });
}



$(function() {
	setupRaty();
	
	carrega_lista();
	
	$('#comnts_submit').click(function(){
        cadastrar_comentario();
    });

});
