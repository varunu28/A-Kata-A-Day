//Least Common Multiple
//Level:5kyu
/*
Problem Description: Write a function that calculates the least common multiple of its arguments; each argument is 
assumed to be a non-negative integer.
*/

var gcd=function(a,b)
{
    var t;
    while(b!==0)
    {
        t=b;
        b=a%b;
        a=t;
    }
    return a;
};

var lcm = function () {
    var inp=[];
    for (var i = 0; i < arguments.length; i++) {
        inp.push(arguments[i]);
  }
  if(inp.length>1)
  {
      var l=inp[0]*inp[1]/gcd(inp[0],inp[1]);
      
      for(i=2;i<inp.length;i++)
      {
          l=l*inp[i]/gcd(l,inp[i]);
      }
      return l;
  }
  else
  {
      return inp[0];
  }
  
};