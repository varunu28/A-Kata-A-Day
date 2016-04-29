//How many are smaller than me?
//Level:7kyu
/*
Write

function smaller(arr)
that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.

For example:

smaller([5, 4, 3, 2, 1]) === [4, 3, 2, 1, 0]
smaller([1, 2, 0]) === [1, 1, 0]
If you've completed this one and you feel like testing your performance tuning of this same kata, head over to the 
much tougher version How many are smaller than me II?
*/

function smaller(nums) {
    var i=0;
    var ans=[];
    while(i<nums.length)
    {
        var j=i+1;
        var count=0;
        while(j<nums.length)
        {
            if(nums[i]>nums[j])
            {
                count++;
            }
            j++;
        }
        ans.push(count);
        i++;
    }
    return ans;
}
