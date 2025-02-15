let list1 = [1, 2, 3]
let list2 = [3,0,1]
let list3 = [0,1]
let list4 = [9,6,4,2,3,5,7,0,1]


function missingNumber(numbers){
    const newSet = new Set(numbers);
    for (let i = 0; i <= numbers.length; i++){
        if(!newSet.has(i)){
            return i
        }
    }
}

console.log(missingNumber(list2)); 