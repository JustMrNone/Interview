
function SpiralMatrix(matrix){
    let ans = [];

    // Continue the loop until the matrix is empty
    while(matrix.length > 0){
        // The spread syntax (...) ensures that elements from the row are added individually, not the row itself.
        ans.push(...matrix.shift());

        // Check if there are any columns left
        if (matrix.length > 0 && matrix[0].length > 0){
            // Add the last element of each remaining row
            for (let i = 0; i < matrix.length; i++){
                ans.push(matrix[i].pop());
            }
        }

        // Check if there are any rows left
        if (matrix.length > 0){
            // Add the last row in reverse order
            ans.push(...matrix.pop().reverse());
        }

        // Check if there are any columns left
        if (matrix.length > 0 && matrix[0].length > 0){
            // Add the first element of each remaining row in reverse order
            for(let i = matrix.length - 1; i >= 0; i--){
                ans.push(matrix[i].shift());
            }
        }

    }

    return ans;
}

const answ = SpiralMatrix([[1,2,3],[4,5,6],[7,8,9]])
console.log(answ);



let spiral = (matrix) => {
    let ans = []

    while (matrix.length > 0){
        ans.push(...matrix.shift())

        if (matrix.length > 0 && matrix[0].length > 0){
            for (let i = 0;i < matrix.length;i++){
                ans.push(matrix[i].pop())
            }
        }
        
        if (matrix.length > 0){
            ans.push(...matrix.pop().reverse())
        }

        if (matrix.length > 0 && matrix[0].length > 0){
            for(let i = matrix.length - 1; i >= 0; i--){
                ans.push(matrix[i].shift())
            }
        }

    }

    return ans;

}

const answer = spiral([[1,2,3],[4,5,6],[7,8,9]])

console.log(answer)
