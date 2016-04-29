//Surface Area and Volume of a Box
//Level:8kyu
/*
Problem Description: Write a function that returns the total surface area and volume of a box as an array:
[area, volume].
*/

function getSize(width, height, depth)
{
    var ans=[];
    var tsa=2*((width*height)+(height*depth)+(depth*width));
    var volume=width*height*depth;
    ans.push(tsa);
    ans.push(volume);
    return ans;
}