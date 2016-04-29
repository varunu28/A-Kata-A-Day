//Unique In Order
//Level: 6kyu
/*
Problem Description: Implement the function unique_in_order which takes as argument a sequence and returns a list of 
items without any elements with the same value next to each other and preserving the original order of elements.

For example:

uniqueInOrder('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
uniqueInOrder('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
uniqueInOrder([1,2,2,3,3])       == [1,2,3]
*/

var uniqueInOrder=function(iterable){
  
  var i=0;
  var ans=[];
  while(i<iterable.length)
  {
      if(iterable[i]!==iterable[i+1])
      {
          ans.push(iterable[i])
      }
      i++;
  }
  return ans;
}