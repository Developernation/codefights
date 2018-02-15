function adjacentElementsProduct(inputArray) {
    var x = inputArray[0] * inputArray[1]
    for (var i = 1; i < inputArray.length; i++){
        if (inputArray[i] * inputArray[i-1] > x){
           x = inputArray[i] * inputArray[i-1]
           
       }       
    }
    return x
}