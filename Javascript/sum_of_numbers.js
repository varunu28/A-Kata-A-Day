//Beginner Series #3 Sum of Numbers
//Level 7kyu
/* 
Problem Description:Given two integers, which can be positive and negative, find the sum of all the numbers between 
including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!
*/

function GetSum( a,b )
{
   var sum=0;
   
   if(a===b)
   {
       sum=a;
   }
   
   else if(a<b)
   {
        while(a<=b)
        {
            sum+=a;
            a++;
        }
   }
   
   else if(b<a)
   {
        while(b<=a)
        {
            sum+=b;
            b++;
        }
   }
   
   return sum;
}

