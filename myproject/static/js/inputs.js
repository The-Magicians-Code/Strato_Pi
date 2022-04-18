function loadval() {
    fetch("/api", {
        method: "POST",
        body: JSON.stringify({
            "motor": 1,
            "value": document.getElementsByName("slider1")[0].value
        })
    })
}

let slider1 = document.getElementById("slider1");

slider1.addEventListener("click", (e) => {
    if (!e.target.matches("input")) {
        waitReading(500);
    }
})
slider1.addEventListener("input", (e) => {
    waitReading(1000);
})


function waitReading(delay) {
    setTimeout(function () {
        loadval()
        console.log(delay);
    },
        delay);
}

function send(values){
    fetch("/form")
}

loadval();