//Playing with digits
//Level: 6kyu
/*
Problem Description: Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find 
a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal 
to k * n. In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.

Note: n, p will always be given as strictly positive integers.
*/

function digPow(n, p){
  var n_str=n.toString();
  var end_pow=p+n_str.length -1;
  
  var sum=0;
  var i=0;
  
  while(i<n_str.length)
  {
      var num=parseInt(n_str[i]);
      sum=sum + Math.pow(num,p);
      i++;
      p++;
  }
  
  var ret_n =1;
  while(true)
  {
      if(n*ret_n===sum)
      {
        return ret_n;
      }
      
      if(n*ret_n>sum)
      {
          return -1;
      }
      
      ret_n++;
  }
}