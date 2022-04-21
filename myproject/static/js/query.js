function getInfo() {
    let data = fetch("/api")
        .then(resp => resp.json())
        .then(d => writeInfo(d));
}

function writeInfo(data) {
    // console.log(data)
    for (let i = 0; i < 3; i++) {
        document.getElementById("power"+i).innerText = data["motor" + i.toString()].power;
        document.getElementById("current"+i).innerText = data["motor" + i.toString()].current;
        document.getElementById("voltage"+i).innerText = data["motor" + i.toString()].voltage;
        document.getElementById("speed"+i).innerText = data["motor" + i.toString()].speed;
        document.getElementById("frequency"+i).innerText = data["motor" + i.toString()].frequency;
    }
}

let update = true;

function myLoop() {
    setTimeout(function() {
        getInfo();
        if (update) {
            myLoop();
        }
    }, 1000)
}

myLoop();
