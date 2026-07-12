// Function to capitalize every first letter of a word
function capitalizeFirstLetter(str) {
  var lower = String(str).toLowerCase().replace("-", " ");
  return lower.replace(/(^| )(\w)/g, function(x) {
    return x.toUpperCase();
  });
}

// Options of the chart
const options = {
  chart: {
    height: "100%",
    maxWidth: "100%",
    type: "line",
    fontFamily: "Inter, sans-serif",
    dropShadow: {
      enabled: false,
    },
    toolbar: {
      show: false,
    },
  },
  tooltip: {
    enabled: true,
    x: {
      show: false,
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    width: 6,
    curve: 'smooth'
  },
  grid: {
    show: true,
    strokeDashArray: 4,
    padding: {
      left: 2,
      right: 2,
      top: -26
    },
  },
  series: [{}],
  legend: {
    show: false
  },
  xaxis: {
    labels: {
      show: true,
      style: {
        fontFamily: "Inter, sans-serif",
        cssClass: 'text-xs font-normal fill-body'
      }
    },
    axisBorder: {
      show: false,
    },
    axisTicks: {
      show: false,
    },
  },
  yaxis: {
    show: false,
  },
}

// Rendering the chart

const chart = new ApexCharts(document.getElementById("line-chart"), options);
chart.render();

let index = 0;

// Adding values to the chart
fetch(`/fragrances/${ids}/history`)
  .then(response => response.json())
  .then(data => {

    var priceArray = {};
    var dateTime = [];
    
    try {
      data.forEach(frag => {
        checkArray()
        function checkArray() {
          if (priceArray[frag.site_name]) {
            priceArray[frag.site_name].push(frag.price);
          } else {
            priceArray[frag.site_name] = [];
            checkArray();
          }
        }
        dateTime.push(new Date(frag.scraped_at).toLocaleDateString('en-US', {month: 'long', day: 'numeric'}));
        })
    } catch (error) {
      console.log("Could not retrieve data");
      document.getElementById("line-chart").remove();
    }

    const keys = Object.keys(priceArray);
    const seriesArray = [];

    for(key of keys) {
      seriesArray.push({
        name: capitalizeFirstLetter(key),
        data: priceArray[key]
    })}

    chart.updateSeries(seriesArray)

    chart.updateOptions({
      xaxis: {
      categories: dateTime,}
    })
})
