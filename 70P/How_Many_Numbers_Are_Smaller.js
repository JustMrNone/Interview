// time complexity is n * n therefore O(n^2) not efficient, I will implement the optimal one later 


let nums = [8,1,2,2,3]



let countSmallest =  (numbers) => {
    let ans = [];
    const leng = numbers.length

    for(let i = 0; i < leng; i++){
        let count = 0;
        for(let j = 0; j < leng; j++){
            if (numbers[j] < numbers[i]){
                count++;
            }
        }
        ans.push(count);
        count = 0;
    }
    return ans
}

function smallers(numbers){
    const copy = [...numbers];
    const temp = copy.sort((a, b) => a - b);
    let hashMap = {};
    let ans = [];

    for (let i = 0; i < temp.length; i++){
        if(!(temp[i] in hashMap)){
            hashMap[temp[i]] = i;
        }
    }
    for (let j = 0; j < nums.length; j++){
        ans.push(hashMap[nums[j]]);
    }
    return ans;
}
console.log(countSmallest(nums));
console.log(smallers(nums));
