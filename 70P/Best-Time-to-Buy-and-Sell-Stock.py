from typing import List

prices1 = [7,1,5,3,6,4]

# The maxProfit function uses a two-pointer technique to find the maximum profit.
# Time complexity: O(n), where n is the number of days. This is because we only pass through the list once.

def maxProfit(prices: List[int]) -> int:
    leftp = 0
    rightp = 1
    maxp = 0
    
    while rightp != len(prices):
        if prices[leftp] < prices[rightp]:
            prof = prices[rightp] - prices[leftp]
            maxp = max(maxp, prof)
        else:
            leftp = rightp 
        rightp += 1
        
    return maxp




# The maxProfit2 function uses a brute-force approach to find the maximum profit.
# Time complexity: O(n^2), where n is the number of days. This is because we use two nested loops to check every pair of days.

def maxProfit2(prices: List[int]) -> int:
    maxp = 0
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                prof = prices[j] - prices[i]
                maxp = max(maxp, prof)
    return maxp
                

