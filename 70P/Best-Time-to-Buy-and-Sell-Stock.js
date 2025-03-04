function maxProfit(prices){
    let maxP = 0;

    for(let i = 0; i < prices.length; i++)
        for(let j = i + 1; j < prices.length; j++)
            if (prices[j] > prices[i]){
                let prof = prices[j] - prices[i];
                maxP = Math.max(maxP, prof)
            }
    return maxP;
}


const prices = [7,1,5,3,6,4]

console.log(maxProfit(prices))

function maxProfitOptimal(prices){
    let leftp = 0;
    let rightp = 1;
    let maxp = 0;

    while (rightp != prices.length){
        if (prices[rightp] > prices[leftp]){
            let profit = prices[rightp] - prices[leftp];
            maxp = Math.max(maxp, profit);
        }else {
            leftp = rightp;
        }
        rightp++;
    }
        
    return maxp;
}


const prices2 = [7,1,5,3,6,4]

console.log(maxProfitOptimal(prices2));