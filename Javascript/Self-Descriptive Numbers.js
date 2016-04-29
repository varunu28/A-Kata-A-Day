//Self-Descriptive Numbers
//Level: 7kyu
/*
Problem Description: A number is self-descriptive when the n'th digit describes the amount n appears in the number.

E.g. 21200:

There are two 0's in the number, so the first digit is 2.

There is one 1 in the number, so the second digit is 1.

There are two 2's in the number, so the third digit is 2.

There are no 3's in the number, so the fourth digit is 0.

There are no 4's in the number, so the fifth digit is 0

Numbers can be of any length up to 9 digits and are only full integers. For a given number derive a function 
selfDescriptive(num) that returns; true if the number is self-descriptive or false if the number is not.
*/

String.prototype.count=function(s1) { 
    return (this.length - this.replace(new RegExp(s1,"g"), '').length) / s1.length;
};

function selfDescriptive(num) {
  num=num.toString();
  var i=0;
  while(i<num.length)
  {
      var check = i.toString();
      //console.log(num.count(check));
      if(parseInt(num.count(check))!==parseInt(num[i]))
      {
          return false;
      }
      i++;
  }
  return true;
}