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
/*slider1.addEventListener("mouseup", (e) => {
    waitReading();
})*/
slider1.addEventListener("click", (e) => {
    if (!e.target.matches("input")) {
        waitReading(500);
    }
})
slider1.addEventListener("input", (e) => {
    waitReading(1000);
})

/*
fetch(`/api/index.php?cmd=add`, {
            method: "POST",
            body: JSON.stringify(update)
        })
            .then(async response => {
                if (response.ok) {
                    return response.json();
                }
                return response.json().then(errorBody => {
                    const error = new Error(response.statusText);
                    error.errorBody = errorBody;
                    throw error;
                });
            })
            .then(data => {
                navigateTo("/?success=true", );
            })
            .catch(error => displayErrors(error.errorBody.errors));
*/


/*x = document.getElementsByName("slider1")[0].value;
x.addEventListener('change', updateValue);*/

function waitReading(delay) {
    setTimeout(function () {
        loadval()
        console.log(delay);
    },
        delay);
}

/*function updateValue(e) {
  x.textContent = e.target.value;
}*/

//console.log(document.getElementsByClassName("rs-tooltip"))

//loadval();
function send(values){
    fetch("/form")
}

loadval();