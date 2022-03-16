class CustomSelect {
    constructor(originalSelect) {

        //Create an grid with div objects
        this.originalSelect = originalSelect;
        this.customSelect = document.createElement("div");
        this.customSelect.classList.add("select", "row", "text-center", "mt-4");

        this.originalSelect.querySelectorAll("option").forEach(optionElement => {

            //make a div object with value
            const itemElement = document.createElement("div");
            itemElement.classList.add("select__item", "col-6");
            this.customSelect.appendChild(itemElement);

            const itemValue = document.createElement("div");
            itemValue.classList.add("h4", "font-weight-bold", "mb-0");
            itemValue.textContent = optionElement.textContent;
            itemElement.appendChild(itemValue);


            //take item value and paste as a text
            var e = document.querySelector("select");
            var value = e.options[e.selectedIndex].value;
            var text = e.options[e.selectedIndex].text;
            const itemSpan = document.createElement("span");
            itemSpan.classList.add("small", "text-gray", "subtext");
            itemSpan.textContent = optionElement.value;
            itemElement.appendChild(itemSpan);

            //if no one is selected, take default
            if (optionElement.selected) {
                this._select(itemElement);
            }


            //selection by click
            itemElement.addEventListener("click", () => {
                if (this.originalSelect.multiple && itemElement.classList.contains("select__item--selected")) {
                    this._deselect(itemElement);
                } else {
                    this._select(itemElement);
                }
            });

        });

        this.originalSelect.insertAdjacentElement("afterend", this.customSelect);
        this.originalSelect.style.display = "none";
    }

    //to select
    _select(itemElement) {
        const index = Array.from(this.customSelect.children).indexOf(itemElement);

        if (!this.originalSelect.multiple) {
            this.customSelect.querySelectorAll(".select__item").forEach(el => {
                el.classList.remove("select__item--selected");
            });
        }

        this.originalSelect.querySelectorAll("option")[index].selected = true;
        itemElement.classList.add("select__item--selected");
    }

    //to deselect
    _deselect(itemElement) {
        const index = Array.from(this.customSelect.children).indexOf(itemElement);
        this.originalSelect.querySelectorAll("option")[index].selected = false;
        itemElement.classList.remove("select__item--selected");
    }
}

document.querySelectorAll(".custom-select").forEach(selectElement => {
    new CustomSelect(selectElement);
});

$("#slider1").roundSlider({
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
    if (document.getElementById("parameter1").selectedIndex == 0) {
        var val = e.value;
        return val + " A";
    } else {
        var val = e.value;
        return val + " C";
    }

}
