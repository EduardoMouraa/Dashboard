$(document).ready(function(){
	var dataTable = $("#dataTable").DataTable()
	var customerChannel = pusher.subscribe('customer');
	customerChannel.bind('add', function(data) {
	var date = new Date();
	var mes = (date.getMonth() + 1).toString()
	var dia = date.getDate().toString()

	if (mes.length == 1){
		mes = "0" + mes
	}
	if (dia.length == 1){
		dia = "0" + dia
	}
	var convert_date = date.getFullYear() +'/'+ mes +'/'+ dia
	dataTable.row.add([
	    data.name,
	    data.position,
	    data.office,
	    data.age,
	    `${convert_date}`,
	    data.salary
	  ]).draw( false );
	  
	  post_date = getTime(new Date)
	  document.getElementById('last-att-pedido').innerText = post_date;
	});

    post_date = getTime(new Date)
	document.getElementById('last-att-pedido').innerText = post_date;
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