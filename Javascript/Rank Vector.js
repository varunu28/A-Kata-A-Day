//Rank Vector
//Level: 6kyu
/*
Problem Description: Given an array (or list) of scores, return the array of ranks for each value in the array. The 
largest value has rank 1, the second largest value has rank 2, and so on. Ties should be handled by assigning the 
same rank to all tied values. For example:

ranks([9,3,6,10]) = [2,4,3,1]
and

ranks([3,3,3,3,3,5,1]) = [2,2,2,2,2,1,7]
because there is one 1st place value, a five-way tie for 2nd place, and one in 7th place.

*/

function ranks(a) {
    var temp = a.slice();
    temp.sort(function(a, b){return b-a});
    
    var i=0;
    var ans=[];
    while(i<a.length)
    {
        ans.push(temp.indexOf(a[i])+1);
        i++;
    }
    return ans;
}