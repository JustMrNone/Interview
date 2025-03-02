function stray(numbers) {
    let ans = numbers.reduce((a, b) => a ^ b);
    return ans;
}

// Solution using frequency count
function stray2(numbers) {
    const count = {};
    for (let num of numbers) {
        count[num] = (count[num] || 0) + 1;
    }
    return Number(Object.keys(count).find(key => count[key] === 1));
}

// Solution using array sorting
function stray3(numbers) {
    numbers.sort((a, b) => a - b);
    return numbers[0] === numbers[1] ? numbers[numbers.length - 1] : numbers[0];
}

// Solution using array filter
function stray4(numbers) {
    return numbers.find(num => 
        numbers.filter(n => n === num).length === 1
    );
}

// Solution using indexOf and lastIndexOf
function stray5(numbers) {
    return numbers.find(num => 
        numbers.indexOf(num) === numbers.lastIndexOf(num)
    );
}