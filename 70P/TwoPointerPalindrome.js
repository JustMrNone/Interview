function IsIt(sentence){
    let sen = sentence.toLowerCase().replace(/[^a-z0-9]/g, '');
    let start = 0;
    let end = sen.length - 1;
    while (start < end){
        if (sen[start] != sen[end]){
            return false;
        }
        start++; 
        end--;
    }
    return true;
}

console.assert(IsIt("asa") === true, "Test Case 1 Failed");
console.assert(IsIt("asq") === false, "Test Case 2 Failed");
console.assert(IsIt("A man a plan a canal Panama") === true, "Test Case 3 Failed");
console.assert(IsIt("No lemon no melon") === true, "Test Case 4 Failed");
console.assert(IsIt("Hello") === false, "Test Case 5 Failed");

console.log("All test cases passed!");