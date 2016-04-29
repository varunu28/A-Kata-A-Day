//Digital Sum
//Level: 6kyu
/*
Problem Description: In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that
value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable
to the natural numbers.

Here's how it works:
digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6
*/

function digital_root(n) {
  var sum;
  var i=0;
  var str;
  
  while(true)
  {
      str=n.toString();
      sum=0;
      i=0;
      while(i<str.length)
      {
          sum+=parseInt(str.charAt(i), 10);
          i++;
      }
      if(sum.toString().length===1)
      {
          n=sum;
          break;
      }
      else
      {
          n=sum;
      }
  }
  return n;
}