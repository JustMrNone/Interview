"use strict";
/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

*/
function findMedianSortedArrays(nums1, nums2) {
    // Make sure nums1 is the shorter array
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1];
    }
    const m = nums1.length;
    const n = nums2.length;
    const totalLength = m + n;
    const half = Math.floor((totalLength + 1) / 2);
    let left = 0;
    let right = m;
    while (left <= right) {
        const partitionX = Math.floor((left + right) / 2);
        const partitionY = half - partitionX;
        // Find the four points around possible median
        const maxLeftX = partitionX === 0 ? -Infinity : nums1[partitionX - 1];
        const minRightX = partitionX === m ? Infinity : nums1[partitionX];
        const maxLeftY = partitionY === 0 ? -Infinity : nums2[partitionY - 1];
        const minRightY = partitionY === n ? Infinity : nums2[partitionY];
        // Check if we found the correct partition
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            // If total length is odd
            if (totalLength % 2 === 1) {
                return Math.max(maxLeftX, maxLeftY);
            }
            // If total length is even
            return (Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
        }
        // If partition is too far to the right
        else if (maxLeftX > minRightY) {
            right = partitionX - 1;
        }
        // If partition is too far to the left
        else {
            left = partitionX + 1;
        }
    }
    throw new Error("Input arrays are not sorted");
}
// Test cases
console.log(findMedianSortedArrays([1, 3], [2])); // Expected: 2.0
console.log(findMedianSortedArrays([1, 2], [3, 4])); // Expected: 2.5
console.log(findMedianSortedArrays([0, 0], [0, 0])); // Expected: 0.0
console.log(findMedianSortedArrays([], [1])); // Expected: 1.0
console.log(findMedianSortedArrays([2], [])); // Expected: 2.0
