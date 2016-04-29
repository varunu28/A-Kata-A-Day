//Equal Sides Of An Array
//Level:6kyu
/*
Problem Description:You are going to be given an array of integers. Your job is to take that array and find an index
N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is 
no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index 
({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index 
({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:

An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negaive.

Output:

The index N such as the side to the left of N is equal to the side to the right of N. If you do not find an index 
that fits these rules, then you will return -1.
*/

function findEvenIndex(arr)
{
    var i=1;
    var ans=-1;
    
    while(i<arr.length)
    {
        var sum1=0;
        var sum2=0;
        
        var j=0;
        var k=i+1;
        
        while(j<i)
        {
            sum1+=arr[j];
            j++;
        }
        
        while(k<arr.length)
        {
            sum2+=arr[k];
            k++;
        }
        
        if(sum1===sum2)
        {
            ans=i;
            break;
        }

        i++;
    }
    return ans;
}