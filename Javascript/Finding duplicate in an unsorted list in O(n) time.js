//Finding duplicate in an unsorted list in O(n) time
//Level:6kyu
/*
Spin-off of this kata, here you will have to figure out an efficient strategy to solve the problem of finding the 
sole duplicate number among an unsorted array/list of numbers starting from 1 up to n.

Hints: a solution in linear time can be found; using the most intuitive ones to search for duplicates that can run 
in O(n²) time won't work.
*/

var findDup=function(arr){
  var check=[];
  var i=0;
  var max_of_array = Math.max.apply(Math, arr);
  while(i<max_of_array)
  {
      check.push(0);
      i++;
  }
  i=0;
  var dup;
  
  while(i<arr.length)
  {
      //console.log(check[arr[i]-1]);
      if(check[arr[i]-1]===0)
      {
          check[arr[i]-1]=1;
      }
      else
      {
          dup=arr[i];
          break;
      }
      i++;
  }
  
  return dup;
};