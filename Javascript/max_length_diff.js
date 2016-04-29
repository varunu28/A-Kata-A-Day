//Maximum length difference
//Level:7kyu
/*Problem Description: You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to
z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 or a2 are empty return -1 in each language except in Haskell where you will return Nothing.

Example:

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(s1, s2) --> 13
*/

function mxdiflg(a1, a2) {
    if(a1.length===0 || a2.length===0)
    {
        return -1;
    }
    
    else
    {
        var a1_len=[];
        var a2_len=[];
        var i=0;
        
        while(i<a1.length)
        {
            a1_len.push(a1[i].length);
            i++;
        }
        
        i=0;
        while(i<a2.length)
        {
            a2_len.push(a2[i].length);
            i++;
        }
        
        
        a1_len.sort(function(a, b){return a-b});
        a2_len.sort(function(a, b){return a-b});
        
        var diff1=Math.abs(a1_len[0]-a2_len[a2.length-1]);
        var diff2=Math.abs(a1_len[a1.length-1]-a2_len[0]);
        
        return Math.max(diff1,diff2);
    }
}
