let prices1: number[] = [7,1,5,3,6,4]




function BestTime(prices: number[]): number{
    let leftp: number = 0;
    let rightp: number = 0; 
    let maxp: number = 0;


    while (rightp < prices.length){
        if (prices[leftp] < prices[rightp]){
            let profit: number = prices[rightp] - prices[leftp];
            maxp = Math.max(maxp, profit);
        } else {
            leftp = rightp;
        }
        rightp++;
    }

    return maxp;
}