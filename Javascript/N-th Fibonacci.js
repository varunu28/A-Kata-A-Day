//N-th Fibonacci
//Level:6kyu
/*
Problem Description: I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci 
Sequence.

For example:

   nthFibo(4) == 2
Because 2 is the 4th number in the Fibonacci Sequence.

For reference, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of
the previous two.
*/

function nthFibo(n) {
    var n1=0;
    var n2=1;
    if(n==1)return n1;
    if(n==2)return n2;
    var count =2;
    while(count!==n)
    {
        var temp=n2;
        n2+=n1;
        n1=temp;
        count++;
    }
    return n2;
}
