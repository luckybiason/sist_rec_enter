$(function(){
	
    // --------------- Validação / Submit --------------- //
    
    //-Função de validação do preenchimento dos campos
	form_enabled_submit = function(){
		//if( $(this).val()!= '')$( ".ui-button[type='submit']" ).button({ disabled: false });
		var flag_fill = true;  
		
		//-Pelo menos um campo dev ser preenchido
		$("form input[type='text'], form textarea ").each(function(){               
		    if( $(this).val()!='') { flag_fill = false; }//pelo menos um preenchido    
		});     
		
		//-Todos os campos obrigatórios devem ter sido preenchidos        
		$(".vObrigatorio").each(function(){     
		    if( $(this).val()=='') { flag_fill = true }//todos devem estar preenchidos
	    });   
	    
	    //-Habilita ou não o botão  
		$( ".ui-button[type='submit']" ).button({ disabled: flag_fill }); 
				
	}
		
	//-Desabilita o botão enquanto não preencher um campo
	//$('form input, form textarea, select').first().focus();
	$( ".ui-button[type='submit']" ).button({ disabled: true }); 
	
	//-Validação de preenchimento
	$('form input, form textarea, select')
	               .live("change", form_enabled_submit)   // qualquer um
	               .live("input", form_enabled_submit)    // inputtext
	               //.live("click", form_enabled_submit)  // checkboxes
	               .live("focus", form_enabled_submit)    // qualquer um
	               .live("keypress", form_enabled_submit) // inputtext
	               .live("keydown", form_enabled_submit)  // inputtext
	               .live("blur", form_enabled_submit);    // qualquer um
	
    //-Submit o formulário ao teclar 'Enter', de qualquer campo texto, textarea ou select 
	$("form input, form textarea").bind('keypress', function(e) {
		var code = (e.keyCode ? e.keyCode : e.which);
		if (code == 13) {//Enter keycode
			form = $(this).closest("form");
			form.submit();
		}
	}); 


	
    // --------------- Validação / Estilos --------------- //
	$( document ).tooltip();

	//-Adiciona um estilo especial a label dos campos obrigatórios
	if(CAMPOS_OBRIGATORIOS){
		for(var i=0; i<CAMPOS_OBRIGATORIOS.length ;i++)
		    $("#id_"+CAMPOS_OBRIGATORIOS[i]).addClass("vObrigatorio");
	}
	$(".vObrigatorio").parent().parent().addClass("input_obrigatorio_label");
	
	//-Manipulação da mensagem de erro/validação
	$('.errorlist').each(function(){
	    $(this).parent().find("input").after( $(this) ).addClass("input_error");
	    $(this).parent().parent().addClass("control-error");
	    $(this).find("li").hide();
	    $(this).parent().find("img").hide();
	    var img_html = "<img src='/static/images/exclamation.gif' alt='"+$(this).find("li").html()+"' title='"+$(this).find("li").html()+"'>";
	    $(this).parent().append(img_html);
	});
	
	
});




/*$('form input').live("blur",  function(e) {
		form_enabled_submit();
		//if( $(this).val()!= '')$( ".ui-button[type='submit']" ).button({ disabled: false });
		var flag_fill = true;  
		$("form input[type='text']").each(function(){               
		    if( $(this).val()!='')               
		    { flag_fill = false }//pelo menos um preenchido    
		});         
		$( ".ui-button[type='submit']" ).button({ disabled: flag_fill }); 
    }); */