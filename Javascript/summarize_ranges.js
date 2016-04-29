//Summarize ranges
//Level: 6kyu
/*
Problem Description: Write

function summaryRanges(nums)
that given a sorted array of numbers, returns the summary of its ranges.
For example:

summaryRanges([1,2,3,4]) === ['1->4']
summaryRanges([0, 1, 2, 5, 6, 9]) === ["0->2", "5->6", "9"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) === ["0->7"]
summaryRanges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) === ["0->7","9->10"]
summaryRanges([-2,0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) ===["-2", "0->7", "9->10", "12"]
summaryRanges([1,1,1,1,1]) === ['1']
*/

Array.prototype.allValuesSame = function() {

    for(var i = 1; i < this.length; i++)
    {
        if(this[i] !== this[0])
            return false;
    }

    return true;
};

function summaryRanges(nums) {
  var i=0;
  var k=0;
  var ans=[];
  var seq=[];
  
  while(i<nums.length)
  {
    
    if(nums[i+1]-nums[i]===1 || nums[i+1]-nums[i]===0)
    {
        seq.push(nums[i]);
    }
    else
    {
        seq.push(nums[i]);
        ans.push(seq);
        seq=[];
    }
    i++;
  }
  
  i=0;
  var str_ans=[];
  while(i<ans.length)
  {
      var int_seq=ans[i];
      if(int_seq.length===1 || int_seq.allValuesSame()===true)
      {
        str_ans.push(int_seq[0].toString());
      }
      else
      {
          str_ans.push(int_seq[0].toString()+'->'+int_seq[int_seq.length-1].toString());
      }
      i++;
  }
  return str_ans;
}
