(function($) {
  'use strict';
  $(function() {
    if ($("#dashboard-rating-1").length) {
      $('#dashboard-rating-1').barrating({
        theme: 'fontawesome-stars',
        showSelectedRating: false,
        initialRating: '2',
      });
    }
    if ($("#dashboard-rating-2").length) {
      $('#dashboard-rating-2').barrating({
        theme: 'fontawesome-stars',
        showSelectedRating: false,
        initialRating: '4',
      });
    }
    if ($("#dashboard-rating-3").length) {
      $('#dashboard-rating-3').barrating({
        theme: 'fontawesome-stars',
        showSelectedRating: false,
        initialRating: '3',
      });
    }
    if ($("#dashboard-rating-4").length) {
      $('#dashboard-rating-4').barrating({
        theme: 'fontawesome-stars',
        showSelectedRating: false,
        initialRating: '1',
      });
    }
    if ($("#dashboard-lineChart").length) {
      var lineChartCanvas = $("#dashboard-lineChart").get(0).getContext("2d");
      var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: {
          labels: ["2013", "2014", "2014", "2015", "2016", "2017"],
          datasets: [{
            data: [2, 4, 3, 3, 2, 3],
            backgroundColor: [
              '#e6f2fb'
            ],
            borderColor: [
              'rgba(102, 16 ,242, 1)'
            ],
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          scales: {
            xAxes: [{
              gridLines: {
                drawBorder: false,
                display: false
              },
              ticks: {
                display: false,
              }
            }],
            yAxes: [{
              gridLines: {
                drawBorder: false,
                display: false,
              },
              ticks: {
                display: false,
              }
            }]
          },
          legend: {
            display: false
          },
          elements: {
            point: {
              radius: 0
            }
          }
        }
      });
    }
    if ($("#dashboard-lineChart-2").length) {
      var lineChartCanvas = $("#dashboard-lineChart-2").get(0).getContext("2d");
      var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: {
          labels: ["2013", "2014", "2014", "2015", "2016", "2017"],
          datasets: [{
            data: [2, 4, 3, 3, 2, 3],
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            backgroundColor: [
              'rgba(0,0,0,0)'
            ],
            borderColor: [
              '#caa8f9'
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          scales: {
            xAxes: [{
              gridLines: {
                drawBorder: false,
                display: false
              },
              ticks: {
                display: false,
              }
            }],
            yAxes: [{
              gridLines: {
                drawBorder: false,
                display: false,
              },
              ticks: {
                display: false,
              }
            }]
          },
          legend: {
            display: false
          },
          tooltips: {
            enabled: false
          },
          layout: {
            padding: {
              top: 5,
              bottom: 5
            }
          }
        }
      });
    }
    if ($("#dashboard-lineChart-3").length) {
      var lineChartCanvas = $("#dashboard-lineChart-3").get(0).getContext("2d");
      var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: {
          labels: ["2013", "2014", "2014", "2015", "2016", "2017"],
          datasets: [{
            data: [2, 4, 3, 3, 2, 3],
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            backgroundColor: [
              'rgba(0,0,0,0)'
            ],
            borderColor: [
              '#fff'
            ],
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          scales: {
            xAxes: [{
              gridLines: {
                drawBorder: false,
                display: false
              },
              ticks: {
                display: false,
              }
            }],
            yAxes: [{
              gridLines: {
                drawBorder: false,
                display: false,
              },
              ticks: {
                display: false,
              }
            }]
          },
          legend: {
            display: false
          },
          tooltips: {
            enabled: false
          },
          layout: {
            padding: {
              top: 5,
              bottom: 5
            }
          }
        }
      });
    }
    if ($("#dashboard-donut-chart").length) {
      $(function() {
        var total = 62;
        var browsersChart = Morris.Donut({
          element: 'dashboard-donut-chart',
          data: [{
              label: "Download Sales",
              value: 12
            },
            {
              label: "In-Store Sales",
              value: 30
            },
            {
              label: "Mail-Order Sales",
              value: 20
            }
          ],
          resize: true,
          colors: ['#03a9f3', '#00c292', '#dddddd'],
          formatter: function(value, data) {
            return Math.floor(value / total * 100) + '%';
          }
        });

        browsersChart.options.data.forEach(function(label, i) {
          var legendItem = $('<span></span>').text(label['label']).prepend('<span>&nbsp;</span>');
          legendItem.find('span')
            .css('backgroundColor', browsersChart.options.colors[i]);
          $('#legend').append(legendItem)
        });
      });
    }
    if ($('#morris-line-example').length) {
      Morris.Line({
        element: 'morris-line-example',
        lineColors: ['#dadada', '#fb9678'],
        data: [{
            y: '2006',
            a: 50,
            b: 0
          },
          {
            y: '2007',
            a: 75,
            b: 78
          },
          {
            y: '2008',
            a: 30,
            b: 12
          },
          {
            y: '2009',
            a: 35,
            b: 50
          },
          {
            y: '2010',
            a: 70,
            b: 100
          },
          {
            y: '2011',
            a: 78,
            b: 65
          }
        ],
        grid: false,
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: "always"
      });
    }
    if ($("#dashboard-monthly-analytics").length) {
      var ctx = document.getElementById('dashboard-monthly-analytics').getContext("2d");
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['Jan', 'Feb', 'Mar', 'Arl', 'May', 'Jun', 'Jul', 'Aug'],
          datasets: [{
              label: "Ios",
              borderColor: 'rgba(171, 140 ,228, 0.8)',
              backgroundColor: 'rgba(171, 140 ,228, 0.8)',
              pointRadius: 0,
              fill: true,
              borderWidth: 1,
              fill: 'origin',
              data: [0, 0, 30, 0, 0, 0, 50, 0]
            },
            {
              label: "Android",
              borderColor: 'rgba(88, 216 ,163, 0.7)',
              backgroundColor: 'rgba(88, 216 ,163, 0.7)',
              pointRadius: 0,
              fill: true,
              borderWidth: 1,
              fill: 'origin',
              data: [0, 35, 0, 0, 30, 0, 0, 0]
            },
            {
              label: "Windows",
              borderColor: 'rgba(255, 180 ,99, 0.7)',
              backgroundColor: 'rgba(255, 180 ,99, 0.7)',
              pointRadius: 0,
              fill: true,
              borderWidth: 1,
              fill: 'origin',
              data: [0, 0, 0, 40, 10, 50, 0, 0]
            }
          ]
        },
        options: {
          maintainAspectRatio: false,
          legend: {
            display: false,
            position: "top"
          },
          scales: {
            xAxes: [{
              ticks: {
                display: true,
                beginAtZero: true,
                fontColor: 'rgba(0, 0, 0, 1)'
              },
              gridLines: {
                display: false,
                drawBorder: false,
                color: 'transparent',
                zeroLineColor: '#eeeeee'
              }
            }],
            yAxes: [{
              gridLines: {
                drawBorder: true,
                display: true,
                color: '#eeeeee',
              },
              categoryPercentage: 0.5,
              ticks: {
                display: true,
                beginAtZero: true,
                stepSize: 20,
                max: 80,
                fontColor: 'rgba(0, 0, 0, 1)'
              }
            }]
          },
        },
        elements: {
          point: {
            radius: 0
          }
        }
      });
      document.getElementById('js-legend').innerHTML = myChart.generateLegend();
    }
    if ($('#morris-area-example').length) {
      var browsersChart = Morris.Area({
        element: 'morris-area-example',
        lineColors: ['#00c292', '#03a9f3'],
        fillOpacity: 0.1,
        xLabelMargin: 10,
        yLabelMargin: 10,
        data: [{
            y: '2006',
            a: 30,
            b: 0
          },
          {
            y: '2007',
            a: 75,
            b: 50
          },
          {
            y: '2008',
            a: 30,
            b: 12
          },
          {
            y: '2009',
            a: 55,
            b: 50
          },
          {
            y: '2010',
            a: 40,
            b: 60
          },
          {
            y: '2011',
            a: 60,
            b: 45
          },
          {
            y: '2012',
            a: 60,
            b: 35
          }
        ],
        grid: false,
        axes: false,
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: "always",
        formatter: function(value, data) {
          return Math.floor(value / total * 100) + '%';
        }
      });
    }
    if ($("#morris-dashboard-bar-chart").length) {
      Morris.Bar({
        element: 'morris-dashboard-bar-chart',
        barColors: ['#fe946b', '#b663e6'],
        barGap: 9,
        barSizeRatio: 0.55,
        hideHover: 'always',
        grid: false,
        data: [{
            y: 'a',
            a: 30,
            b: 40
          },
          {
            y: 'b',
            a: 55,
            b: 65
          },
          {
            y: 'c',
            a: 60,
            b: 70
          },
          {
            y: 'd',
            a: 55,
            b: 45
          },
          {
            y: 'e',
            a: 40,
            b: 45
          }
        ],
        xkey: 'y',
        ykeys: ['a', 'b'],
        axes: 'x',
        labels: ['Series A', 'Series B']
      });
    }
    if($("#growth-chart").length) {
      $("#growth-chart").sparkline('html', {
        enableTagOptions: true,
        type: 'bar',
        width: '100%',
        height: '50',
        fillColor: 'false',
        barColor: '#fb9678',
        barWidth: 4,
        barSpacing: 4,
        chartRangeMin: 0
      });
    }
  });
})(jQuery);