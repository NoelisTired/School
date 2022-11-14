function MyButton() {
    if (document.getElementById('button').innerHTML == 'Lees Meer') { //? If the button says 'Lees Meer'
        document.getElementById('leesmeer').style = "display: block"; //? Shows the lorem
        document.getElementById('button').innerHTML = "Lees Minder"; //? Overwrites the button text
    } else {
        document.getElementById("leesmeer").style = "display: none"; //? Hides the lorem
        document.getElementById('button').innerHTML = "Lees Meer"; //? Overwrites the button text
    }
}

//!  Alternative Method
//? document.addEventListener("click", function () {});