const belvishColour = "#4B0A58";
const whiffColour = "#1447E6";
const aarColour = "#FF6B6B";
const palaceColour = "#4ECDC4";
const havenColour = "#FFE66D";


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
      data: [6500, 6418, 6456, 6526, 6356, 6456],
      color: belvishColour,
    },
    {
      name: "Whiff Culture",
      data: [6456, 6356, 6526, 6332, 6418, 6500],
      color: whiffColour,
    },
        {
      name: "Aar Fragrances",
      data: [6500, 6418, 6456, 6526, 6356, 6456],
      color: aarColour,
    },
    {
      name: "Perfume Palace",
      data: [6456, 6356, 6526, 6332, 6418, 6500],
      color: palaceColour,
    },
        {
      name: "Fragrance Haven",
      data: [6500, 6418, 6456, 6526, 6356, 6456],
      color: havenColour,
    },
  ],
  legend: {
    show: false
  },
  xaxis: {
    categories: ['01 Feb', '02 Feb', '03 Feb', '04 Feb', '05 Feb', '06 Feb', '07 Feb'],
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

if (document.getElementById("line-chart") && typeof ApexCharts !== 'undefined') {
  const chart = new ApexCharts(document.getElementById("line-chart"), options);
  chart.render();
}
