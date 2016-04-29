//Exes and Ohs
//Level 7kyu
/*Instructions: Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and 
be case insensitive. The string can contains any char.

Examples input/output:
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

*/

function XO(str) {
    str=str.toLowerCase(); // To consider the case insensitive part
    var num_o=0; // Count for number of o's
    var num_x=0; // Count for number of x's
    var i=0;     // Counter for looping through every character of the string
    
    while(i<str.length)
    {
        if(str[i]==='o')
        {
            num_o++;
        }
        else if(str[i]==='x')
        {
            num_x++;
        }
        i++;
    }
    
    if(num_x===num_o)
    {
        return true;
    }
    else
    {
        return false;
    }
}

