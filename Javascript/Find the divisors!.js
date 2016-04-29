//Find the divisors!
//Level:6kyu
/*
Problem Description: Create a function named divisors that takes an integer and returns an array with all of the 
integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime'
(use Either String a in Haskell).

Example:

divisors(12); //should return [2,3,4,6]
divisors(25); //should return [5]
divisors(13); //should return "13 is prime"
You can assume that you will only get positive integers as inputs.
*/

function divisors(integer) {
    var div = [];
    var n=2;
    while(n<=integer/2)
    {
        if(integer%n===0)
        {
            div.push(n);
        }
        n++;
    }
    if(div.length===0)
    {
        return integer.toString()+" is prime";
    }
    else
    {
        return div;
    }
}
