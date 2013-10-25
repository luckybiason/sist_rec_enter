$(function() {

	//- Esconder/Mostrar captchas
	esconder_captchas = function() {
		$('#line_captcha').hide();
		$('#ebcaptchainput').parent().hide();
	}
	mostrar_captchas = function() {
		$('#line_captcha').show();
		$('#ebcaptchainput').parent().show();
	}
	validar_login = function() {
		if ($("#id_login").val() != "" & $("#id_senha").val() != "") {
			mostrar_captchas();
		} else {
			esconder_captchas();
		}
	}
	esconder_captchas();

	//- Previnir submit no enter
	$('#form_login').bind("keypress", function(e) {
		//esconderCarregando();
		if (e.keyCode == 13) {
			e.preventDefault();
			return false;
		}
	});

	//- Senha/Login abre o captcha keypress
	$('#id_login, #id_senha').on("input",  validar_login)
	                         .on("blur",   validar_login)
	                         .on("focus",  validar_login)
	                         .on("change", validar_login);

});
