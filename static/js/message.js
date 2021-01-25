$(document).ready(function () {
  (function($) {
    "use strict";

    // Configure tooltips for collapsed side navigation
    $('.navbar-sidenav [data-toggle="tooltip"]').tooltip({
      template: '<div class="tooltip navbar-sidenav-tooltip" role="tooltip" style="pointer-events: none;"><div class="arrow"></div><div class="tooltip-inner"></div></div>'
    })
    post_date = getTime(new Date)
    document.getElementById('last-time-messages').innerText = post_date;
    // Configure tooltips globally
    $('[data-toggle="tooltip"]').tooltip()
  })(jQuery);

  var messageChannel = pusher.subscribe('message');

  // Listen to 'message sent' event
  messageChannel.bind('send', function(data) {
    var message = document.getElementById('message-count')
    var date = new Date();
    var toAppend = document.createElement('a')
    toAppend.classList.add('list-group-item', 'list-group-item-action')
    toAppend.href = '#'
    document.getElementById('message-box').appendChild(toAppend)
    var hours = date.getHours().toString()
    var minutes = date.getMinutes().toString()
    
    if (hours.length == 1){
      hours = "0" + hours
    }
    if (minutes.length == 1){
      minutes = "0" + minutes
    }

    if (data.message.length > 40){
      data.message = data.message.substring(0,40) + "..."
    }
    var mes = (date.getMonth() + 1).toString()
    var dia = date.getDate().toString()
  
    if (mes.length == 1){
      mes = "0" + mes
    }
    if (dia.length == 1){
      dia = "0" + dia
    }
    var convert_date = date.getFullYear() +'/'+ mes +'/'+ dia
    post_date = hours+ ':' + minutes
    toAppend.innerHTML ='<div class="media">'+
                    '<img class="d-flex mr-3 rounded-circle" src="http://placehold.it/45x45" alt="">'+
                    '<div class="media-body">'+
                      `<strong>${data.name}</strong> postou uma nova mensagem: `+
                      `<textarea rows="1" cols="46" style="resize: none; border:none;" disabled>${data.message}</textarea>`+
                      `<div class="text-muted smaller">${convert_date} às ${post_date}</div>`+
                    '</div>'+
                  '</div>'
    message.innerText = parseInt(message.innerText)+1

    post_date = getTime(new Date)
    document.getElementById('last-time-messages').innerText = post_date;
  });
});

function getTime(date){
  var hours = date.getHours().toString()
  var minutes = date.getMinutes().toString()
  
  if (hours.length == 1){
    hours = "0" + hours
  }
  if (minutes.length == 1){
    minutes = "0" + minutes
}

return hours+ ':' + minutes
}