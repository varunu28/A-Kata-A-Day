//longest_palindrome
//Level: 6kyu
/*
Problem Description: Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
*/

isPalin=function(s)
{
    return s===s.split("").reverse().join("");
};

longestPalindrome=function(s)
{
    if(s.length===1)
    {
        return 1;
    }
    if(s.length===0)
    {
        return 0;
    }
    var i=0;
    var n=1;
    while(i<s.length)
    {
        j=i+1;
        while(j<s.length)
        {
            //console.log(s.substring(i,j+1));
            if(isPalin(s.substring(i,j+1)))
            {
                //console.log(s.substring(i,j+1));
                if(s.substring(i,j+1).length>n)
                {
                    n=s.substring(i,j+1).length;
                }
            }
            j++;
        }
        i++;
    }
    return n;
};