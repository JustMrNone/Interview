// the time complexity is O(n/2) and we drop constant factors so O(n) the time growa linearly 
// if you see O(n/3), O(2n), or O(5n), they all simplify to O(n) because they all scale linearly.

function isIt(mystr){
    const lowerdString = mystr.toLowerCase();
    let start = 0;
    let end = mystr.length - 1

    while(start < end){

        if (lowerdString[start] != lowerdString[end]){
            return false;
        } 

        start++;
        end--;
    }

    return true;
}

const ex1 = isIt("civic");
const ex2 = isIt("Radar");
const ex3 = isIt("ability");

console.log(ex1, ex2, ex3);