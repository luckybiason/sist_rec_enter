$(function() {

	$.extend({
		alert : function(message, title) {
			$("<div></div>").dialog({
				buttons : {
					"Ok" : function() {
						$(this).dialog("close");
					}
				},
				close : function(event, ui) {
					$(this).remove();
				},
				resizable : false,
				title : title,
				modal : true
			}).text(message);
		}
	});

//plugin de mini caixa de confirmação //
            $('.ask-plain').live('click',function(e) {
				e.preventDefault();
				thisHref = $(this).attr('href');
				if (confirm('Are you sure')) { window.location = thisHref; }
			});
	
			$('.ask').live('click',function(e) {
				e.preventDefault();
				thisHref = $(this).attr('href');
				if ($(this).next('div.question').length <= 0)
				    $(this).after('<div class="question">Tem certeza?<br/><a class="yes link_btn">Sim</a><a class="cancel link_btn">Não</a></div>');
				$('.question').animate({opacity : 1}, 300);
				$('.yes').live('click', function() { 
					window.location = thisHref; 
					});
				$('.cancel').live('click', function() { 
					$(this).parents('div.question').fadeOut(300, function() { 
						$(this).remove(); 
					}); 
					return false;
				});
			    $(".yes,.cancel").button();
	            $(".question").addClass("ui-widget-content").css("text-align","center!important");
			});
			
//plugin de alerta desconhecido //
        var myMessages = ['info','warning','error','success'];
        function hideAllMessages(){
			 var messagesHeights = new Array(); // this array will store height for each
			 for (i=0; i<myMessages.length; i++){
					  messagesHeights[i] = $('.' + myMessages[i]).outerHeight(); // fill array
					  $('.' + myMessages[i]).css('top', -messagesHeights[i]-50); //move element outside viewport	  
			 }
         }
         function showMessage(type, message){
			$('.'+ type +'-trigger').click(function(){
				  hideAllMessages();
				  if(message) $('.'+type).html(message);
				  $('.'+type).animate({top:"-15"}, 500);
			});
		}
		$(document).ready(function(){
		 
		 // Initially, hide them all
		 hideAllMessages();
		 
		 // Show message
		 for(var i=0;i<myMessages.length;i++){showMessage(myMessages[i],'');}
		 
		 // When message is clicked, hide it
		 $('.message').click(function(){			  
				  $(this).animate({top: -$(this).outerHeight()-50}, 500);
		  });		 
		 
        });  
});