//Object Literal aka Python Dictionary

//one way to make an object
var josh = {
    name:'Joshua',
    lastName:'Smoshua',
    job:'Teacher',
    married:false,
    age:27,
}
//the other way to make an object

var timmeh = new Object();
//-------------------------------------

console.log(josh);

//accessing values in Object Literals
var j_name = josh.name;
var j_job = josh['job'];//notice it uses a string

console.log(j_name);
console.log(j_job);

//-----change a value------------
var change_lst_nm = josh.lastName = 'Roberts';
var change_job = josh['job'] = 'Fish monger';

console.log(change_lst_nm);
console.log(change_job);
console.log(josh);

//----now TIMMEH-------------------
timmeh.name = 'Timothy';
timmeh.age = '78';
timmeh.married = true;

console.log(timmeh);

//---------functions statements in js objects--------------

var employee = {
    first_name: 'Bill',
    last_name: 'Nye',
    dept: 'Science',
    birth_month: 'March',
    birth_date: '12',
    birth_year: 1975,
    //this is how you write a func statement in an Object and add/change
    //attributes
    calculateAge: function() {
        this.age = 2017 - this.birth_year;
    }
    
}
employee.calculateAge();

console.log(employee);