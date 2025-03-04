let nums: number[] = [-4,-1,0,3,10];


function SquaredSorted(numbs: number[]): number[]{
    let Squared: number[] = [];
    for(let i = 0; i < numbs.length; i++){
        Squared.push(numbs[i] ** 2)
    }
    Squared.sort((a, b) => a - b);
    return Squared;
}

console.log(SquaredSorted(nums));