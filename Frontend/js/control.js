class CustomSelect {
    constructor(originalSelect) {

        //Create a grid with div objects
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

class Slider1 {
    constructor(_max_value, _step) {
        const Arr_slider1 = Array.from($('.slider1'));

        Arr_slider1.forEach(el => $(el).roundSlider({
            sliderType: "min-range",
            radius: 120,
            width: 20,
            circleShape: "pie",
            startAngle: 315,
            lineCap: "round",
            max: _max_value,
            step: _step,

            svgMode: true,
            borderWidth: 0,
            pathColor: "#ddd",
            rangeColor: "#0dcaf0",
            value: 0,
            tooltipFormat: "changeTooltip",
            change: "traceChange",
        }))


    }
}

class Slider2 {
    constructor(_max_value, _step) {
        const Arr_slider2 = Array.from($('.slider2'));

        Arr_slider2.forEach(el => $(el).roundSlider({
            sliderType: "min-range",
            radius: 120,
            width: 20,
            circleShape: "pie",
            startAngle: 315,
            lineCap: "round",
            max: _max_value,
            step: _step,

            svgMode: true,
            borderWidth: 0,
            pathColor: "#ddd",
            rangeColor: "#0dcaf0",
            value: 0,
            tooltipFormat: "changeTooltip",
            change: "traceChange",
        }))


    }
}

class Slider3 {
    constructor(_max_value, _step) {

        const Arr_slider3 = Array.from($('.slider3'));

        Arr_slider3.forEach(el => $(el).roundSlider({
            sliderType: "min-range",
            radius: 120,
            width: 20,
            circleShape: "pie",
            startAngle: 315,
            lineCap: "round",
            max: _max_value,
            step: _step,

            svgMode: true,
            borderWidth: 0,
            pathColor: "#ddd",
            rangeColor: "#0dcaf0",
            value: 0,
            tooltipFormat: "changeTooltip",
            change: "traceChange",
        }))


    }
}
//Slider selection depending on selected value
const selection1 = Array.from(document.getElementById("parameter1").children);
selection1.forEach(el => addEventListener('click', (event) => {
    const index1 = $("select[id='parameter1'] option:selected").index();
    if (index1 === 0) {
        let slider1 = new Slider1(10, 0.1);
        window.changeTooltip = function (e) {
            return e.value + "A";
        }
    } else if (index1 === 1) {
        let slider1 = new Slider1(380, 1);
        window.changeTooltip = function (e) {
            return e.value + "V";
        }
    } else if (index1 === 2) {
        let slider1 = new Slider1(100, 1);
        window.changeTooltip = function (e) {
            return e.value + "%";
        }
    } else if (index1 === 3) {
        let slider1 = new Slider1(50, 1);
        window.changeTooltip = function (e) {
            return e.value + "Hz";
        }
    } else if (index1 === 4) {
        let slider1 = new Slider1(1450, 1);
        window.changeTooltip = function (e) {
            return e.value + "RPM";
        }
    };
}));

const selection2 = Array.from(document.getElementById("parameter2").children);
selection2.forEach(el => addEventListener('click', (event) => {
    const index2 = $("select[id='parameter2'] option:selected").index();
    if (index2 === 0) {
        let slider2 = new Slider2(10, 0.1);
        window.changeTooltip = function (e) {
            return e.value + "A";
        }
    } else if (index2 === 1) {
        let slider2 = new Slider2(380, 1);
        window.changeTooltip = function (e) {
            return e.value + "V";
        }
    } else if (index2 === 2) {
        let slider2 = new Slider2(100, 1);
        window.changeTooltip = function (e) {
            return e.value + "%";
        }
    } else if (index2 === 3) {
        let slider2 = new Slider2(50, 1);
        window.changeTooltip = function (e) {
            return e.value + "Hz";
        }
    } else if (index2 === 4) {
        let slider2 = new Slider2(1450, 1);
        window.changeTooltip = function (e) {
            return e.value + "RPM";
        }
    };
}));

const selection3 = Array.from(document.getElementById("parameter3").children);
selection3.forEach(el => addEventListener('click', (event) => {
    const index3 = $("select[id='parameter3'] option:selected").index();
    if (index3 === 0) {
        let slider3 = new Slider3(10, 0.1);
        window.changeTooltip = function (e) {
            return e.value + "A";
        }
    } else if (index3 === 1) {
        let slider3 = new Slider3(380, 1);
        window.changeTooltip = function (e) {
            return e.value + "V";
        }
    } else if (index3 === 2) {
        let slider3 = new Slider3(100, 1);
        window.changeTooltip = function (e) {
            return e.value + "%";
        }
    } else if (index3 === 3) {
        let slider3 = new Slider3(50, 1);
        window.changeTooltip = function (e) {
            return e.value + "Hz";
        }
    } else if (index3 === 4) {
        let slider3 = new Slider3(1450, 1);
        window.changeTooltip = function (e) {
            return e.value + "RPM";
        }
    };
}));