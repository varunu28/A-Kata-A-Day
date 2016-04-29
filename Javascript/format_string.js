//Format a string of names
//Level: 6kyu
/*
Problem Description: Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be 
separated by an ampersand.

Example:
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''

*/


function list(names){
  
  var output = [];
    for (var n=0; n < names.length ; ++n)
        output.push(names[n]["name"]);
    
    var ans="";
    var i=0;
    if(output.length===1)
    {
        ans=output[0];
    }
    else
    {
        while(i<output.length)
        {
            if(i===output.length-2)
            {
                ans+=output[i]+" & "+output[i+1];
                break;
            }
            else
            {
                ans+=output[i]+", ";
            }
            i++;
        }  
    }
    
    
    return ans;
}