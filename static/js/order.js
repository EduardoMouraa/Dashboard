// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
// -- Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", 'Junho'],
    datasets: [{
      label: "Receita",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [0, 0, 0, 0, 0, 0],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          beginAtZero: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

Pusher.logToConsole = true;

// Configure Pusher instance
var pusher = new Pusher('6763e719a40167a6a7db', {
  cluster: 'us2',
  encrypted: true
});

// Subscribe to poll trigger
var orderChannel = pusher.subscribe('order');

var date = new Date().getMonth()
// Listen to 'order placed' event
var order = document.getElementById('order-count')
orderChannel.bind('place', function(data) {
  myLineChart.data.datasets.forEach((dataset) => {
    if (parseInt(data.month) == 6 || parseInt(data.month) == 12) {
      dataset.data[-1] = data.units
    }else{
      dataset.data[parseInt(data.month) - 1] = data.units
    }
      console.log(parseInt(data.month) - 1, data.units)
  });
  myLineChart.update();
  order.innerText = parseInt(order.innerText)+1

  post_date = getTime(new Date)
	document.getElementById('last-time-receita').innerText = post_date;
});
post_date = getTime(new Date)
document.getElementById('last-time-receita').innerText = post_date;

// use data from database
var valores = JSON.parse(document.getElementById('valores').value.replaceAll("'", '"')) ;

for (var dado in valores){

  myLineChart.data.datasets.forEach((dataset) => {
    dataset.data[parseInt(dado.substr(1,1)) - 1] = valores[dado]
  });
  myLineChart.update();
  order.innerText = parseInt(order.innerText)+1
}

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