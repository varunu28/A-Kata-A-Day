//Find factors of a number
//Level:7kyu
/*
Problem Description:Create a function that takes a number and finds the factors of it, listing them in descending 
order in an array.

If the parameter is not an integer or less than 1, return -1. In C# return an empty array.

For Example: factors(54) should return [54, 27, 18, 9, 6, 3, 2, 1]
*/

function factor(x)
{
    var ans=[];
    var i=1;
    if(x===1)
    {
        ans=[1];
        return ans;
    }
    while(i<=x/2)
    {
        if(x%i===0)
        {
            ans.push(i);
        }
        i++;
    }
    
    ans.push(x);
    
    return ans.reverse();
}

function factors(x){
    if (x === parseInt(x, 10) && x>=1)
    {
        return factor(x);
    }
    else
    {
        return -1;
    }
}