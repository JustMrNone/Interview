let nums1 = [1,2,3,1]
let nums2 = [1,2,3,4]


function containsDuplicates(nums){
    return new Set(nums).size !== nums.length;
}

console.log(containsDuplicates(nums1));
console.log(containsDuplicates(nums2));