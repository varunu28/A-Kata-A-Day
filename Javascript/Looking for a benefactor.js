//Looking for a benefactor
//Level: 7kyu
/*
Problem Description:The accounts of the "Fat to Fit Club (FFC)" association are supervised by John as a volunteered 
accountant. The association is funded through financial donations from generous benefactors. John has a list of the 
first n donations: [14, 30, 5, 7, 9, 11, 15] He wants to know how much the next benefactor should give to the 
association so that the average of the first n + 1 donations should reach an average of 30. After doing the math he 
found 149. He thinks that he made a mistake. Could you help him?

if dons = [14, 30, 5, 7, 9, 11, 15] then new_avg(dons, 30) --> 149

The function new_avg(arr, navg) should return the expected donation (rounded up to the next integer) that will 
permit to reach the average navg. Should the last donation be a non positive number (<= 0) John wants us to throw an
error (return Nothing in Haskell) so that he clearly sees that his expectations are not great enough.

Notes:

all donations are numbers, arr can be empty.
See examples below to see which error is to be thrown.
newAvg([14, 30, 5, 7, 9, 11, 15], 92) should return 645
newAvg([14, 30, 5, 7, 9, 11, 15], 2) should throw new RangeError 
*/

function newAvg(arr, newavg) {
    var n = arr.length;
    var new_tot = newavg*(n+1);
    var curr_tot=0;
    var i=0;
    while(i<n)
    {
        curr_tot+=arr[i];
        i++;
    }
    if(curr_tot<new_tot)
    {
        return Math.ceil(new_tot-curr_tot);
    }
    else
    {
        throw new RangeError();
    }
}