//X marks the spot!
//Level:6kyu
/*
Problem Description: Write a function x(n) that takes in a number n and returns an nxn array with an X in the middle.
The X will be represented by 1's and the rest will be 0's. 
E.g.

x(5) === [[1, 0, 0, 0, 1],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 1, 0],
          [1, 0, 0, 0, 1]];

x(6) === [[1, 0, 0, 0, 0, 1],
          [0, 1, 0, 0, 1, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 0, 1, 1, 0, 0],
          [0, 1, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 1]];
*/

function x(n) {
    var ans=[];
    var i=0;
    
    while(i<n)
    {
        var j=0;
        var a=[];
        while(j<n)
        {
            a[j]=0;
            j++;
        }
        ans.push(a);
        i++;
    }
    
    i=0;
    while(i<n)
    {
        var k=0;
        while(k<n)
        {
            if(i===k)
            {
                ans[i][k]=1;
            }
            if(i+k===n-1)
            {
                ans[i][k]=1;
            }
            k++;
        }
        i++;
    }
    return ans;
}