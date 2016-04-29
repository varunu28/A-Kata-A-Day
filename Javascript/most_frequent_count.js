//Find Count of Most Frequent Item in an Array
//Level: 7kyu
/*
Write a JavaScript program to find count of the most frequent item of an array.

Assume that input is array of integers.

Ex.:

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5
Most frequent number in example array is -1. It occures 5 times in input array.
*/

function mostFrequentItemCount(collection) {
    collection.sort(function(a, b){return a-b});
    var i=0;
    var ans=[];
    var int_ans=[];
    while(i<collection.length)
    {
        if(collection[i]===collection[i+1])
        {
            int_ans.push(collection[i]);
        }
        else
        {
            int_ans.push(collection[i]);
            ans.push(int_ans);
            int_ans=[];
        }
        i++;
    }
    
    var high_count=0;
    
    i=0;
    while(i<ans.length)
    {
        if(ans[i].length>high_count)
        {
            high_count=ans[i].length;
        }
        i++;
    }
    return high_count;
}