
let num = 3;
let hash = "#";
let space = " "
for (let i = 0; i < num; i++){
    let spaces = space.repeat(num - i - 1);
    let hashes = hash.repeat(2 * i + 1);
    let ans = spaces + hashes + spaces
    console.log(ans);
}
console.log("\n")
for (let j = 0; j < num; j++){
    let lefthashes = hash.repeat(2 * j + 1);
    console.log(lefthashes);
}
console.log("\n")
for (let i = 1; i <= num; i++) {
    let hashes = hash.repeat(i);  // Increase hashes normally
    let spaces = " ".repeat(num - i); // Add spaces AFTER hashes to align right

    console.log(spaces + hashes);
}