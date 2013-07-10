function AdicionarFiltro(tabela, coluna) {
    var indice =  coluna.index()+1;
    var cols = $("#" + tabela + " thead tr:first-child th").length;
    var colFiltrar = $("#" + tabela + " thead tr:nth-child(1) th:nth-child(" + indice + ")");
    $(colFiltrar).parent().parent().prepend("" + coluna.text() + ":<select id='filtroColuna_" + indice + "'  class='filtroColuna'> </select>");
    var valores = new Array();
    $("#" + tabela + " tbody tr").each(function () {
        var txt = $(this).children("td:nth-child(" + indice + ")").text();
        if (valores.indexOf(txt) < 0) {
            valores.push(txt);
        }
    });
    $("#filtroColuna_" + indice).append("<option>TODOS</option>")
    for (elemento in valores) {
        $("#filtroColuna_" + indice).append("<option>" + valores[elemento] + "</option>");
    }
    $("#filtroColuna_" + indice).change(function () {
        var filtro = $(this).val();
        $("#" + tabela + " tbody tr").show();
        if (filtro != "TODOS") {
            $("#" + tabela + " tbody tr").each(function () {
                var txt = $(this).children("td:nth-child(" + indice + ")").text();
                if (txt != filtro) {
                    $(this).hide();
                }
            });
        }
    });
 
};

function criarTabela(tabela,coluna){
    criarCabecalho(tabela, coluna);
    criarSorter(tabela);
    criarFilter(tabela);
}

function criarCabecalho(tabela, id){
    $("#"+ tabela + " thead tr th").each(function(){
        if ($(this).attr('id')==id){
            AdicionarFiltro(tabela, $(this) );
        }
    });
}

function criarSorter(tabela){
        $("#"+tabela).tablesorter();
}

function filter(campo,tabela){
	var encontrou = false;
	var termo = campo.val().toLowerCase();
	$('#'+tabela+' tbody tr').each(function(){
		$(this).find('td').each(function(){
		  if($(this).text().toLowerCase().indexOf(termo) > -1) encontrou = true;
		});
		if(!encontrou) $(this).hide();
		else $(this).show();
		encontrou = false;
	  });
}
function criarFilter(tabela){
	$('#pesquisarForm').toggle();
        $('#pesquisar').keydown(function(){ filter($(this),tabela) })
                       .blur(function(){ filter($(this),tabela) });
}
