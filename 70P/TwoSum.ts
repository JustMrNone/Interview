let numbers1: number[] = [2, 11, 7, 15];
const tar: number = 9;
// O(N)
function twoSums(nums: number[], target: number): number[]{
    const hashMap: Record<number, number> = {}
    for (let i = 0; i < nums.length; i++){
        const diff: number = target - nums[i]
        if (diff in hashMap){
            return [i, hashMap[diff]];
        }
        hashMap[nums[i]] = i
    }
    return []
}

// O(n * n)
function twoSumBruteForce(nums: number[], target: number): number[]{
    const ans: number[] = [];
    for(let i = 0; i < nums.length; i++){
        for(let j = i + 1; j < nums.length; j++){
            if(nums[i] + nums[j] == target){
                ans.push(i, j);
            }
        }
    }
    return ans;
}

console.log(twoSums(numbers1, tar));
console.log(twoSumBruteForce(numbers1, tar));

