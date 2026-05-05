// Colour of the chart lines

const belvishColour = "#4B0A58";
const whiffColour = "#1447E6";
const aarColour = "#FF6B6B";
const palaceColour = "#4ECDC4";
const havenColour = "#FFE66D";

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
  series: [
    {
      name: "Belvish",
      data: [],
      color: belvishColour,
    },
    {
      name: "Whiff Culture",
      data: [],
      color: whiffColour,
    },
        {
      name: "Aar Fragrances",
      data: [],
      color: aarColour,
    },
    {
      name: "Perfume Palace",
      data: [],
      color: palaceColour,
    },
        {
      name: "Fragrance Haven",
      data: [],
      color: havenColour,
    },
  ],
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

fetch(`https://frag-track-app.onrender.com/fragrances/${ids}/history`)
  .then(response => response.json())
  .then(data => {

    const belvishArray = [];
    const whiffArray = [];
    const aarArray = [];
    const palaceArray = [];
    const havenArray = [];
    const dateTime = [];

    data.forEach(frag => {
        belvishArray.push(frag[index+2])
        whiffArray.push(frag[index+3])
        aarArray.push(frag[index+4])
        palaceArray.push(frag[index+5])
        havenArray.push(frag[index+6])
        console.log(frag[index+7])
        dateTime.push(new Date(frag[index+7].split(" ")[0]).toLocaleDateString('en-US', {month: 'long', day: 'numeric'}))
    })

    chart.updateSeries([
            {
        name: "Belvish",
        data: belvishArray,
        color: belvishColour,
        },
            {
        name: "Whiff Culture",
        data: whiffArray,
        color: whiffColour,
        },
            {
        name: "Aar Fragrances",
        data: aarArray,
        color: aarColour,
        },
        {
        name: "Perfume Palace",
        data: palaceArray,
        color: palaceColour,
        },
            {
        name: "Fragrance Haven",
        data: havenArray,
        color: havenColour,
        }
    ])

    chart.updateOptions({
        xaxis: {
            categories: dateTime,
        }
    })
})
