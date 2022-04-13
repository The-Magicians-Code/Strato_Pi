function butonas() {
    b1 = []
    b2 = []
    b3 = []

    for (let i = 1; i < 10; i++) {
        b1.push(document.getElementById("Button1" + i.toString()).id)
    }

    for (let i = 1; i < 8; i++) {
        b2.push(document.getElementById("Button2" + i.toString()).id)
    }
    
    for (let i = 1; i < 8; i++) {
        b3.push(document.getElementById("Button3" + i.toString()).id)
    }

    console.log(b1, b2, b3)
}