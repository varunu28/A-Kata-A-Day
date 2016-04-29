//How many twos?
//Level:7kyu
/*
Problem Description: Write a function that returns the number of '2's in the factorization of a number.
For example,

twoCount(24)
should return 3, since the factorization of 24 is 2^3 x 3

twoCount(17280)
should return 7, since the factorization of 17280 is 2^7 x 5 x 3^3
The number passed to two_count (twoCount) will always be a positive integer greater than or equal to 1.
*/

function twoCount(n) {
  var count=0;
  while(true)
  {
      if(n%2===0)
      {
          count++;
          n/=2;
      }
      else
      {
          break;
      }
  }
  return count;
}
