$(function(){
    $('#list').on('click', function(e){
        visualVitrineList();
    });
    $('#galery').on('click', function(e){
        visualVitrineGal();
    });
});

visualVitrineGal = function(e){
    var ref = $('#items-vitrine');
    ref.addClass('vitrine-galeria');
}
visualVitrineList = function(e){
    var ref = $('#items-vitrine');
    ref.removeClass('vitrine-galeria');
}
