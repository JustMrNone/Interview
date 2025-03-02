function isItPalindrome(sentence: string): boolean {
    let sen: string = sentence.toLowerCase().replace(/[^a-z0-9]/g, '');
    let start: number = 0;
    let end: number = sen.length - 1;
    let ans: boolean = false;

    while (start < end){
        if (sen[start] != sen[end]){
            return ans;
        }
        start++;
        end--;
        ans = true;        
    }
    return ans;
}

console.assert(isItPalindrome("asa") === true, "Test Case 1 Failed");
console.assert(isItPalindrome("asq") === false, "Test Case 2 Failed");
console.assert(isItPalindrome("A man a plan a canal Panama") === true, "Test Case 3 Failed");
console.assert(isItPalindrome("No lemon no melon") === true, "Test Case 4 Failed");
console.assert(isItPalindrome("Hello") === false, "Test Case 5 Failed");

console.log("All test cases passed!");

//tsc --project tsconfig.json
//tsc .\twopointers.ts --target ESNext