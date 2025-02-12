document.addEventListener("DOMContentLoaded", function () {
    let ten = 10;
    let hau = 100;
    
    // Get elements
    let numTen = document.querySelector("#num10");
    let numHau = document.querySelector("#num100");
    let number1 = document.querySelector(".number1");
    let number2 = document.querySelector(".number2");
    let number3 = document.querySelector(".number3");

    // Set initial values
    numTen.innerHTML = ten;
    numHau.innerHTML = hau;

    // Get buttons (using escaped characters for + and -)
    const tenp = document.querySelector("#ten\\+");
    const tenm = document.querySelector("#ten\\-");
    const haup = document.querySelector("#hau\\+");
    const haum = document.querySelector("#hau\\-");
    const infip = document.querySelector("#infi\\+");
    const infim = document.querySelector("#infi\\-");

    function addOne(number) {
        number.innerHTML++;
    }
    
    function minusOne(number) {
        number.innerHTML--;
    }

    /* Add click handlers
    tenp.addEventListener("click", () => addOne(number1));
    tenm.addEventListener("click", () => minusOne(number1));
    haup.addEventListener("click", () => addOne(number2));
    haum.addEventListener("click", () => minusOne(number2));
    infip.addEventListener("click", () => addOne(number3));
    infim.addEventListener("click", () => minusOne(number3));
    */

    tenp.onclick = function () {
    addOne(number1)
        if (number1.innerHTML == 10) {
            number1.innerHTML = 0;
        };
    }

    tenm.onclick = function(){
    minusOne(number1);
        if (number1.innerHTML <= 0){
            number1.innerHTML = 0;
        }
    } 

    haup.onclick = function(){
    addOne(number2);
        if (number2.innerHTML == 100){
            number2.innerHTML = 0;
        }
    }

    haum.onclick = function(){
    minusOne(number2);
        if (number2.innerHTML <= 0){
            number2.innerHTML = 0;
        }
    }

    infip.onclick = function(){
    addOne(number3);
    }
    infip.onclick = function(){
    minusOne(number3);
    if (number3.innerHTML <= 0){
        number3.innerHTML = 0;
    }
    }


});