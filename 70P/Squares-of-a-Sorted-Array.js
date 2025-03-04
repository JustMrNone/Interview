let nums = [-4,-1,0,3,10]

function SquaredSorted(numbers){
    let squared = [];
    for(let i = 0; i < numbers.length; i++){
        squared.push(nums[i] ** 2);
    }
    squared.sort((a, b) => a - b);
    return squared;
}



console.log(SquaredSorted(nums))