//Formatting decimal places
//Level:7kyu
/*
Problem Description:Each number should be formatted that only the first two decimal places are returned. You don't 
need to check whether the input is a valid number because only valid numbers are used in the tests.

Don't round the numbers! Just cut them after two decimal places!

Right examples:  
32.8493 is 32.84  
14.3286 is 14.32

Incorrect examples (e.g. if you round the numbers):  
32.8493 is 32.85  
14.3286 is 14.33
*/

function twoDecimalPlaces(number) {
  var num_str=number.toString();
  var n=num_str.indexOf('.');
  var ans=num_str.substring(0,n)+num_str.substring(n,n+3);
  return parseFloat(ans); //Do not return a string
}
