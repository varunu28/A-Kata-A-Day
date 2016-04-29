//Find The Parity Outlier
//Level 6kyu 
/* Instructions: You are given an array (which will have a length of at least 3, but could be very large) containing
 integers. The integers in the array are either entirely odd or entirely even except for a single integer N. Write a
 method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160

*/


function findOutlier(args){
  var i=0;
  var n,m;
  n=m=0;
  var ans;
  while(i<3) // Just check the first 3 elements to find if the set is of all odd but 1 or all even but 1
  {
    if(Math.abs(args[i])%2===0)
    {
        n++;
    }
    else
    {
        m++;
    }
    i++;
  }
  
  if(n>m) // Parity outlier check for all even but 1 set 
  {
      i=0;
    while(i<args.length)
    {
        if(Math.abs(args[i])%2===1)
        {
            ans=args[i];
            break;
        }
        i++;
    }
  }
  
  else // Parity outlier check for all even but 1 set
  {
      i=0;
    while(i<args.length)
    {
        if(Math.abs(args[i])%2===0)
        {
            ans=args[i];
            break;
        }
        i++;
    }
  }
  return ans; // The parity outlier
}