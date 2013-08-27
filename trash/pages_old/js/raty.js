 $(function() {
	setupRaty();

 
});

var setupRaty = function(){
$.fn.raty.defaults.path = './img/rating/';
    $('#rat').raty({
       halfShow: false,
       score   : 3
    });
}