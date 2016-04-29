//Excessively Abundant Numbers
//Level:7kyu
/*
Problem Description:An abundant number or excessive number is a number for which the sum of its proper divisors is 
greater than the number itself.

The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).

Derive function abundantNumber(num)/abundant_number(num) which returns true/True if num is abundant, false/False if 
not.
*/

function abundantNumber(num) {
    var sum=1;
    var i=2;
    while(i<=Math.ceil(num/2))
    {
        if(num%i===0)
        {
            sum+=i;
        }
        i++;
    }
    if(sum>num)
    {
        return true;
    }
    else
    {
        return false;
    }
}
