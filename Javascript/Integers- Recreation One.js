//Integers: Recreation One
//Level:6kyu
/*
Problem Description: Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 
196, 441, 1764. The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is 
itself a square. 42 is such a number.

The result will be an array of arrays, each subarray having two elements, first the number whose squared divisors is
a square and then the sum of the squared divisors.

Examples:

listSquared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
listSquared(42, 250) --> [[42, 2500], [246, 84100]]
*/

function listSquared(m, n) {
    var sum_arr=[];
    var num_arr=[];
    
    while(m<=n)
    {
        num_arr.push(m);
        var i=1;
        var sum=0;
        while(i<=m)
        {
            if(m%i===0)
            {
                sum+=i*i;
            }
            i++;
        }
        sum_arr.push(sum);
        m++;
    }
    
    var ans_arr=[];
    var j=0;
    while(j<sum_arr.length)
    {
        var temp=[];
        var k=Math.round(Math.sqrt(sum_arr[j]));
        if(k*k===sum_arr[j])
        {
            temp.push(num_arr[j]);
            temp.push(sum_arr[j]);
            ans_arr.push(temp);
        }
        j++;
    }
    return ans_arr;
}