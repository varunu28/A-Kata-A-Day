//Triple trouble
//Level:6kyu
/*
Problem Description: Write a function

tripledouble(num1,num2) which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
For example:
tripledouble(451999277, 41177722899) == 1 // num1 has straight triple 999s and 
                                          // num2 has straight double 99s

tripledouble(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

tripledouble(12345, 12345) == 0

tripledouble(666789, 12345667) == 1
If this isn't the case, return 0
*/

function tripledouble(num1, num2) {
    num1=num1.toString();
    num2=num2.toString();
    var flag1=0;
    var flag2=0;
    
    var n1=[];
    var n2=[];
    
    var i=0;
    while(i<num1.length-2)
    {
        if(num1[i]===num1[i+1] && num1[i+1]===num1[i+2])
        {
            flag1=1;
            n1.push(num1[i]);
            
        }
        i++;
    }
    
    if(flag1===0)
    {
        return 0;
    }
    else
    {
        i=0;
        while(i<num2.length-1)
        {
            if(num2[i]===num2[i+1])
            {
                flag2=1;
                n2.push(num2[i]);
            }
            i++;
        }
    }
    if(flag2===0)
    {
        return 0;
    }
    else
    {
        var c=0;
        i=0;
        
        while(i<n1.length)
        {
            var j=0;
            while(j<n2.length)
            {
                if(n1[i]===n2[j])
                {
                    c=1;
                    i=n1.length;
                    break;
                }
                j++;
            }
            i++;
        }
        return c;
    }
}
