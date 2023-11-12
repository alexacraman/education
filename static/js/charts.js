Highcharts.chart('container', {
    data: {
      table: 'datatable'
    },
    chart: {
      type: 'column',
      
    },
    colors: ['#0c4a6e'],
    title: {
      text: 'Course Achievement(s)'
    },
    xAxis: {
      type: 'category'
    },
    yAxis: {
      allowDecimals: false,
      title: {
        text: 'Percent %'
      }
    },
    tooltip: {
    formatter: function () {
        const myTd = document.getElementById('expDate')
        const expDate = myTd.dataset.exp;

      // return '<p>You achieved</p> ' + this.point.y +  '%  in ' + this.point.name.toLowerCase() + '<br><p> Expires ' + expDate + '</p>' ;
      return '<p>You achieved</p> ' + this.point.y +  '%  in ' + this.point.name.toLowerCase();
        
    }
  }
  });

