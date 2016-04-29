//Finding Remainder Without Using '%' Operator
//Level:7kyu
/*
Problem Description: You have to write a function remainder which takes two arguments : D(Dividend) and d(Divisor) and
returns the remainder when D(Dividend) is divided by d(Divisor).

Assumptions:

The Arguments will always be an Integer.
D(Dividend) will always be greater than or equal to d(Divisor).
Note:

Make sure that the implemented remainder function works exactly same as the Modulus Operator(%) does i.e. m % 0 = NaN 
∀ m ∈ ℕ the only difference would be that here 'NaN' will be a string.
*/

var remainder = function(D,d){
    if(d===0)
    {
      return "NaN";
    }
    else
    {
      return D- Math.floor(D/d)*d;
    }
}