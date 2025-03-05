function isIt(str: string): boolean{
    let sen: string = str.toLowerCase().replace(/[^a-z0-9]/g, '')    
    let leftp = 0;
    let rightp = sen.length - 1;

    while (leftp < rightp){
        if(sen[leftp] != sen[rightp]){
            return false;
        }
        rightp--;
        leftp++;
    }
    return true;
}
console.assert(isIt("asa") == true, "Check Code");
console.assert(isIt("asa") === true, "Test Case 1 Failed");
console.assert(isIt("asq") === false, "Test Case 2 Failed");
console.assert(isIt("A man a plan a canal Panama") === true, "Test Case 3 Failed");
console.assert(isIt("No lemon no melon") === true, "Test Case 4 Failed");
console.assert(isIt("Hello") === false, "Test Case 5 Failed");

console.log("All test cases passed!");

console.log(isIt("asa"));
console.log(isIt("aww"));