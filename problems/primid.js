
let num = 3;
let hash = "#";
let space = " ";

console.log("\n");


for (let i = 0; i < num; i++){
    let spaces = space.repeat(num - i - 1);
    let hashes = hash.repeat(2 * i + 1);
    let ans = spaces + hashes + spaces
    console.log(ans);
}

console.log("\n")
for (let j = 0; j < num; j++){
    let lefthashes = hash.repeat(j + 1);
    console.log(lefthashes);
}
console.log("\n")
for (let i = 1; i <= num; i++) {
    let hashes = hash.repeat(i);  // Increase hashes normally
    let spaces = " ".repeat(num - i); // Add spaces AFTER hashes to align right

    console.log(spaces + hashes);
}

console.log("\n");

for (let g = num; g >= 0; g--) {
    let hashes = hash.repeat(g);
    console.log(hashes)
}

for (let h = num; h >= 0; h--) {
    let hashes = hash.repeat(h);
    let spaces = space.repeat(num - h);
    console.log(spaces + hashes);
}

for (let l = num - 1; l >= 0; l--) {
    let spaces = space.repeat(num - l);
    let hashes = hash.repeat(2 * l + 1);
    console.log(spaces + hashes + spaces)
}