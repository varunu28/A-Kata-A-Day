//Insert dashes
//Level 7kyu
/* 
Problem Description: Write a function insertDash(num) that will insert dashes ('-') between each two odd numbers in 
num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
*/

function insertDash(num) {
   var n = num.toString();
   var ans='';
   var i=0;
   while(i<n.length)
   {
       
       if(parseInt(n[i])%2!==0 && parseInt(n[i+1])%2!==0 && i!==n.length-1) 
       {
           ans=ans+n[i]+'-';
       }
       else if(parseInt(n[i])%2!==0 && parseInt(n[i+1])%2!==0 && i===n.length-1)
       {
           ans=ans+n[i];
       }
       else
       {
           ans=ans+n[i];
       }
       i++;
   }
   return ans;
}

