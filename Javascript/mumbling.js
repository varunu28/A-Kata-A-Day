//Mumbling
//Level: 7kyu
/*
Problem Description: This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") --> "A-Bb-Ccc-Dddd"
accum("RqaEzty") --> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") --> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
*/

function accum(s) {
	var s_arr=s.split("");
	var ans="";
    var i=0;
    while(i<s_arr.length)
    {
        var mid_ans=s_arr[i].toUpperCase();
        ans+=mid_ans;
        
        var n=i;
        while(n>0)
        {
            ans+=s_arr[i].toLowerCase();
            n--;
        }
        
        if(i!=s_arr.length-1)
        {
            ans+="-";
        }
        
        i++;
    }
    return ans;
}