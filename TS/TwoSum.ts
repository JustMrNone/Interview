function twoSum(nums: number[], target: number): number[]{
    let hashMap: Record<number, number> = {}

    for (let i = 0; i < nums.length; i++){
        let difference = target - nums[i];
        if (difference in hashMap){
            return [i, hashMap[difference]];
        }
        hashMap[nums[i]] = i;
    }
    return [];
}



function TwoSum2(nums: number[], target: number): number[]{
    let hashMap: Record<number, number> = {};
    for (let i = 0; i <= nums.length; i++){
        let diff = target - nums[i];
        if (diff in hashMap) return [i, hashMap[diff]];
        hashMap[nums[i]] = i;
    }
    return [];
}

function twoSumSlow(nums: number[], target: number): number[]{
    let indecies:  number[] = [];
    let leng: number = nums.length;  
    for (let i = 0; i < leng; i++)
        for (let j = i + 1; j < leng; j++)
            if(nums[i] + nums[j] === target) 
                indecies.push(i, j);
    return indecies;
}

function TwoSumFast(nums: number[], target: number): number[] {
    let hashMap: Record<number, number> = {};
    for (let i = 0; i < nums.length; i++){
        if (target - nums[i] in hashMap) return [i, hashMap[target - nums[i]]];
        hashMap[nums[i]] = i;
    }
    return [];
}