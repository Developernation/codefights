//-------------CODE Challenge 2 kind of-----------------------------
/*
1. Create array of dates
2. create empty object/hashmap/dictionary
3. fill the empty object with names and ages
4. create a function that tells you if the person is of age 
*/
function ageCheck (keyObj){
    var keyObj;
    var ageVerif = (2018 - keyObj) > 18
    var age = 2018 - keyObj
    return [keyObj[0],ageVerif, age];
}

function upDateObject (arr1, arr2,myObj){
    var arr1, arr2;
    var x; 
    if (arr1.length === arr2.length){
        for (x = 0; x < arr1.length;x++){
            //adds to the object
            myObj[arr2[x]] = [arr1[x]];
            //sets the value of the object to a list 
            myObj[arr2[x]] = ageCheck(myObj[arr2[x]]);              
        }
    return myObj
    }
    return alert('Array length unequal')   
}
//-----------main--------------------------------
var dateArray = new Array(1984,1983,2008);
var names = ['Kelly','Sim','Josiah'];
var namesObj = new Object();

var res = upDateObject(dateArray,names,namesObj);
console.log(res);

