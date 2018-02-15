function checkPalindrome(inputString) {
    return [...inputString].reverse().join("") === inputString; 
}