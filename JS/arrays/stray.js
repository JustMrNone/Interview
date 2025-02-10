function stray(numbers) {
    let ans = numbers.reduce((a, b) => a ^ b);
    return ans;
  }