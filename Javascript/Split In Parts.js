//Split in Parts
//Level:7kyu
/*
Problem Description: The aim of this kata is to split a given string into different strings of equal size (note size
 of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
Assumptions:

String length is always greater than 0
String has no spaces
Size is always positive
*/

var splitInParts = function(s, partLength)
{
    var ans="";
    var i=0;
    while(i<s.length)
    {
        if(s.length-i<=partLength)
        {
            ans+=s.substring(i,s.length);
            break;
        }
        else
        {
            ans+=s.substring(i,i+partLength);
            ans+=" ";
            i+=partLength;
        }
    }
    return ans;
};
