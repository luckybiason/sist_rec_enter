$(function() {
	criarFilter("listagem");
});

function filter(campo, tabela) {
	var encontrou = false;
	var termo = campo.val().toLowerCase();
	$('#' + tabela + ' tbody tr').each(function() {
		$(this).find('td').each(function() {
			if ($(this).text().toLowerCase().indexOf(termo) > -1)
				encontrou = true;
		});
		if (!encontrou)
			$(this).hide();
		else
			$(this).show();
		encontrou = false;
	});
}

function criarFilter(tabela) {
	$('#formPesq').show();
	$('#pesquisar').keydown(function() {
		filter($(this), tabela)
	}).blur(function() {
		filter($(this), tabela)
	});
}