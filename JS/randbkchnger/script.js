const colors = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#A833FF",
    "#33FFF5", "#F5FF33", "#FF8C33", "#8C33FF", "#33FFA8",
    "#A8FF33", "#FF3333", "#33A8FF", "#57FF33", "#FF5733",
    "#FF33F5", "#33F5FF", "#F533FF", "#5733FF", "#33FF8C"
];

const body = document.body;
let hex = document.querySelector(".Hex")

function getRandNumber(){
    const randIndex = Math.floor(colors.length * Math.random());
    return randIndex;
}

function setRandColor(){
    const color = colors[getRandNumber()];
    hex.innerHTML = color;
    body.style.backgroundColor = color;
}

const btn = document.querySelector(".btn");
btn.onclick = setRandColor;