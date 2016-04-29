//Backwards Read Primes
//Level: 6kyu
/*
Problem Description: Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a
different prime. (This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

Task

Find all Backwards Read Primes between two positive given numbers (both inclusive), the second one being greater 
than the first one. The resulting array or the resulting string will be ordered following the natural order of the 
prime numbers.

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
*/

function isPrime(n)
{
    if(n==2 || n==3)return true;
    else if(n%2===0 || n%3===0)return false;
    else{
        var i=5;
        while(i<=n/2)
        {
            if(n%i===0)
            {
                return false;
            }
            i++;
        }
    }
    return true;
}

function backwardsPrime(start, stop){
    var ans=[];
    while(start<=stop)
    {
        if(start>10)
        {
            if(start.toString()!==start.toString().split("").reverse().join(""))
            {
                if(isPrime(start) && isPrime(parseInt(start.toString().split("").reverse().join(""))))
                {
                    ans.push(start);
                }
            }
        }
        start++;
    }
    return ans;
}