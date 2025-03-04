//brute force 

const prices1 = [7,1,5,3,6,4]

function bestTime(prices: number[]): number{
    let maxp = 0;

    for(let i = 0; i < prices.length; i++){
        for(let j = i + 1; j < prices.length; j++){
            if (prices[j] > prices[i]){
                let profit = prices[j] - prices[i];
                maxp = Math.max(maxp, profit); 
            }
        } 
    }
    return maxp;
}


function bestTimeON(prices: number[]): number{
    let left: number = 0;
    let right: number = 1;
    let maxp: number = 0;

    while (right != prices.length){
        if(prices[right] > prices[left]){
            let profit: number = prices[right] - prices[left];
            maxp = Math.max(maxp, profit);
        }else{
            left = right;
        }
        right++;
    }

    return maxp;
}


function bestTimeON2(prices: number[]): number{
    let left: number = 0;
    let right: number = 1;
    let maxp: number = 0;

    while(right != prices.length){
        if(prices[right] > prices[left]){
            let profit: number = prices[right] - prices[left];
            maxp = Math.max(maxp, profit);
        } else {
            left = right
        }
        right++;
    }
    return maxp;
}


console.assert(bestTimeON(prices1) === 5, "Something is wrong")
console.assert(bestTimeON2(prices1) === 5, "Something is wrong")
console.log("Test Passed");
console.log("ans: " +  bestTime(prices1))
