$("#slider1").roundSlider({
    sliderType: "min-range",
    radius: 120,
    width: 20,
    circleShape: "pie",
    startAngle: 315,
    lineCap: "round",
    max: 0.75,
    step : 0.01,

    svgMode: true,
    borderWidth: 0,
    pathColor: "#ddd",
    rangeColor: "#0dcaf0",
    value: 0,
    tooltipFormat: "changeTooltip",
});

$("#slider2").roundSlider({
    sliderType: "min-range",
    radius: 120,
    width: 20,
    circleShape: "pie",
    startAngle: 315,
    lineCap: "round",
    max: 0.75,
    step: 0.01,

    svgMode: true,
    borderWidth: 0,
    pathColor: "#ddd",
    rangeColor: "#0dcaf0",
    value: 0,
    tooltipFormat: "changeTooltip",
});

$("#slider3").roundSlider({
    sliderType: "min-range",
    radius: 120,
    width: 20,
    circleShape: "pie",
    startAngle: 315,
    lineCap: "round",
    max: 1.5,
    step: 0.01,

    svgMode: true,
    borderWidth: 0,
    pathColor: "#ddd",
    rangeColor: "#0dcaf0",
    value: 0,
    tooltipFormat: "changeTooltip",
});

function changeTooltip(e) {
    var val = e.value
    return val + " kW";
}