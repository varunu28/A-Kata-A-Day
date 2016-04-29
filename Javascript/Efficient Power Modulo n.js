//Efficient Power Modulo n
//Level:5kyu
/*
Problem Description: Your task is to create a new implementation of modpow so that it computes (x^y)%n for large y. 
The problem with the current implementation is that the output of Math.pow is so large on our inputs that it won't 
fit in a 64-bit float.

You're also going to need to be efficient, because we'll be testing some pretty big numbers.
*/

function modpow(a, b, n) {
    var res=1;
    while (b)
    {
        if (b % 2) { res = (res * a) % n; }
    
        a = (a * a) % n;
        b =Math.floor(b/2);
    }

    return res;
    
}