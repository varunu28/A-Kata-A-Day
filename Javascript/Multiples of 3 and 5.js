//Multiples of 3 and 5
//Level:6kyu
/*
Problem Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Courtesy of ProjectEuler.net
*/

function solution(number){
    var sum=0;
    var i=1;
    while(i<number)
    {
        if(i%3===0 || i%5===0)
        {
            sum+=i;
        }
        i++;
    }
    return sum;
}