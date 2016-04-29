//Alternating Loops
//Level:6kyu
/*
Problem Description: Write a function combine()that combines arrays by alternatingly taking elements passed to it.

E.g

combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
Arrays can have different lengths.
*/

function combine() {
   var argsArray = Array.prototype.slice.call(arguments);
   
   var max_len=0;
   
   var i=0;
   while(i<argsArray.length)
   {
       if(max_len<argsArray[i].length)
       {
           max_len=argsArray[i].length;
       }
       i++;
   }
   
   var ans=[];
   
   i=0;
   while(i<max_len)
   {
       var j=0;
       while(j<argsArray.length)
       {
           if(i<argsArray[j].length)
           {
               ans.push(argsArray[j][i]);
           }
           j++;
       }
       i++;
   }
   
   return ans;
}