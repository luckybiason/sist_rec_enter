$(function(){
    $('#list').on('click', function(e){
    	e.preventDefault();
        visualVitrineList();
    });
    $('#galery').on('click', function(e){
    	e.preventDefault();
        visualVitrineGal();
    });
});

visualVitrineGal = function(e){
    var ref = $('#items-vitrine');
    ref.addClass('vitrine-galeria');
    $("#galery").addClass('galery-actived');
    $("#list").removeClass('list-actived');
}
visualVitrineList = function(e){
    var ref = $('#items-vitrine');
    ref.removeClass('vitrine-galeria');
    $("#galery").removeClass('galery-actived');
    $("#list").addClass('list-actived');
}
