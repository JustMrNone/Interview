

const numbers = [2, 11, 7, 15]
const target = 9
function twoSum(nums, tar){
    let indexes = []
    const leng = nums.length
    for (let i = 0; i <= leng; i++){
        for(let j = i + 1; j <= leng; j++){
            if(nums[i] + nums[j] == tar){
                indexes.push(i, j)
            }
        }
    }
    return indexes
}

function twoSumON(nums, tar){
    let hashMap = {}

    for (let i = 0; i <= nums.length; i++){
        let diff = target - nums[i]
        if (diff in hashMap){
            return [i, hashMap[diff]]
        }
        hashMap[nums[i]] = i
    }
    return []
}
console.assert(
    JSON.stringify(twoSum(numbers, target)) === JSON.stringify([0, 2]),
    "Test failed: Expected [0, 2]"
);
console.log(twoSum(numbers, 9))

console.log(twoSumON(numbers, 9))