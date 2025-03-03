"use strict";
function twoSum(nums, target) {
    let hashMap = {};
    for (let i = 0; i < nums.length; i++) {
        let difference = target - nums[i];
        if (difference in hashMap) {
            return [i, hashMap[difference]];
        }
        hashMap[nums[i]] = i;
    }
    return [];
}
function TwoSum2(nums, target) {
    let hashMap = {};
    for (let i = 0; i <= nums.length; i++) {
        let diff = target - nums[i];
        if (diff in hashMap)
            return [i, hashMap[diff]];
        hashMap[nums[i]] = i;
    }
    return [];
}
function twoSumSlow(nums, target) {
    let indecies = [];
    let leng = nums.length;
    for (let i = 0; i <= leng; i++)
        for (let j = i + 1; j <= leng; j++)
            if (nums[i] + nums[j] === target)
                indecies.push(i, j);
    return indecies;
}
console.log(twoSumSlow([2, 11, 7, 15], 9));