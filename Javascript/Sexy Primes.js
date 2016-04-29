//Sexy Primes <3
//Level: 7kyu
/*
Problem Description: Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is to complete the
function sexy_prime(x, y) which returns true if x & y are sexy, false otherwise.

Examples:

sexy_prime(5,11)
--> True

sexy_prime(61,67)
--> True

sexy_prime(7,13)
--> True

sexy_prime(5,7)
--> False

sexy_prime(1,7)
--> False
( 1 is not considered prime )
Note: x & y are always positive integers > 0, but they are not always in order of precendence...you can be given 
either (5,11) or (11,5). Both are equally valid.
*/

function isPrime(n)
{
    if(n===1)return false;
    if(n===2)return true;
    if(n%2===0)return false;
    var i=3;
    while(i<=n/2)
    {
        if(n%i===0)return false;
        i++;
    }
    return true;
}

function sexy_prime(x, y){
    if(isPrime(x) && isPrime(y))
    {
        if(x-y===6 || y-x===6)
        {
            return true;
        }
    }
    return false;
}