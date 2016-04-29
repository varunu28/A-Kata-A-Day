//find the odd int
//Level: 6kyu
/*
Problem Description: Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
*/

function findOdd(A) {
  var n=0;
  var ans;
  while(n<A.length)
  {
      var indexes = [], i;
        for(i = 0; i < A.length; i++)
            if (A[i] === A[n])
                indexes.push(i);
        
        if(indexes.length%2===1)
        {
            ans=A[n];
            break;
        }
        n++;
  }
  return ans;
}