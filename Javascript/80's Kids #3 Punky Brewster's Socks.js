//80's Kids #3: Punky Brewster's Socks
//Level:7kyu
/*
Problem Description: Punky loves wearing different colored socks, but Henry can't stand it.

Given an array of different colored socks, return a pair depending on who was picking them out.

Example:

getSocks('Punky',['red','blue','blue','green']) -> ['red', 'blue']
Note that punky can have any two colored socks, in any order, as long as they are different and both exist. Henry 
always picks a matching pair.

If there is no possible combination of socks, return an empty array.
*/

function getSocks(name, socks) 
{
    socks.sort();
    var i=0;
    var c=0;
    var ans=[];
    if(name==='Punky')
    {
        while(i<socks.length)
        {
            if(i!==socks.length-1)
            {
                if(socks[i]!==socks[i+1])
                {
                    ans.push(socks[i]);
                    ans.push(socks[i+1]);
                    c=1;
                    break;
                }
            }
            i++;
        }
    }
    else if(name==='Henry')
    {
        while(i<socks.length)
        {
            if(i!==socks.length-1)
            {
                if(socks[i]===socks[i+1])
                {
                    ans.push(socks[i]);
                    ans.push(socks[i+1]);
                    c=1;
                    break;
                }
            }
            i++;
        }
    }
    if(c===1)
    {
        return ans;
    }
    else
    {
        return [];
    }
}