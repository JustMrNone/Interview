//Input: nums = [4,3,2,7,8,2,3,1]
//Output: [5,6]

let nums1 = [4,3,2,7,8,2,3,1]

let nums2 = [1,1]

function findAll(numbs){
    const setN = new Set(numbs);
    const n = numbs.length;
    let ans = [];

    for (let i = 1; i <= n; i++){
        if(!setN.has(i)){
            ans.push(i);
        }
    }

    return ans
}

let theAns = findAll(nums2);

console.log(theAns);