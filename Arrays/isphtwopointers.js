function isPhil(string){
    let start = 0;
    let end = string.length - 1;

    while (start < end ){
        if (string[start] != string[end]){
            return false;
        }
        start++;
        end--;
    }
    return true;
}

const ans = isPhil("ada");
console.log(ans);