var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Doctorants', 'Doctorantes'],
        datasets: [{
            data: [287,100],
            backgroundColor: [
                '#FEB4A9',
                '#214E77'
            ],
            borderRadius: 50,
        }]
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    display: false,
                    color: 'transparent' // Définir la couleur de la ligne de grille à transparent
                }
            }]
        },
        barPercentage: 0.3,
        
    }
});


var ctx2 = document.getElementById('chart').getContext('2d');
var chart2 = new Chart(ctx2, {
    type: 'doughnut',
  data: {
    labels: ['Doctorants', 'Doctorantes'],
        datasets: [{
            data: [287,100],
            backgroundColor: [
                '#FEB4A9',
                '#214E77'
            ],
        }],
  },
  options: {

    cutoutPercentage: 30,
    responsive: true,
    maintainAspectRatio: false,
    aspectRatio: 2,
  }
});