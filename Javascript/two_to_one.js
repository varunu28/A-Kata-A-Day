//Two to One
//Level 7kyu
/* 
Problem Description:Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the 
longest possible, containing distinct letters, - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
*/

function longest(s1,s2) {
    s1=s1.split("");
    s2=s2.split("");
    
    var new_s=s1.concat(s2);
    
    new_s=new_s.sort();
    
    var ans_s=[];
    
    for(var i=0;i<new_s.length;i++)
    {
        if(ans_s.indexOf(new_s[i])===-1)
        {
            ans_s.push(new_s[i]);
        }
    }
    
    ans_s=ans_s.join("");
    
    return ans_s;
}