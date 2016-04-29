//Multiplication Tables
//Level:6kyu
/*
Problem Description: Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create 
a multiplication table sized according to the given dimensions. **The return value of the function must be an array,
and the numbers must be Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in 
its first column.
*/

function multiplicationTable(row,col){
    var i=0;
    var ans=[];
    while(i<row)
    {
        var j=0;
        var sub_arr=[];
        while(j<col)
        {
            sub_arr.push((i+1)*(j+1));
            j++;
        }
        ans.push(sub_arr);
        i++;
    }
    return ans;
}