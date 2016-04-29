//Surrounding Primes for a value
//Level:6kyu
/*
Problem Description:
We need a function prime_bef_aft() that gives the largest prime below a certain given value n,

befPrime or bef_prime (depending on the language),

and the smallest prime larger than this value,

aftPrime/aft_prime (depending on the language).

The result should be output in a list like the following:

primeBefAft == [befPrime, aftPrime]
If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:

primeBefAft(100) == [97, 101]

primeBefAft(97) == [89, 101]

primeBefAft(101) == [97, 103]
Happy coding!!
*/

function isPrime(m)
{
    if(m===1)
    {
        return false;
    }
    if(m===2)
    {
        return true;
    }
    if(m%2===0)
    {
        return false;
    }
    var i=3;
    while(i<=m/2)
    {
        if(m%i===0)
        {
            return false;
        }
        i++;
    }
    return true;
}
function primeBefAft(num) {
    var ans=[];
    var bef=num-1;
    var aft=num+1;
    
    while(true)
    {
        if(isPrime(bef))
        {
            ans.push(bef);
            break;
        }
        bef--;
    }
    
    while(true)
    {
        if(isPrime(aft))
        {
            ans.push(aft);
            break;
        }
        aft++;
    }
    
    return ans;
}