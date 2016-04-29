//Return String of First Characters
//Level:7kyu
/*
Problem Description: In this exercise, a string is passed to a method and a new string has to be returned with the 
first character of each word in the string

example: 'This Is A Test' will return 'TIAT' 
*/

function makeString(s){
  var ret=[];
  var s_arr=s.split(" ");
  var i=0;
  while(i<s_arr.length)
  {
      ret.push(s_arr[i][0]);
      i++;
  }
  var ans='';
  i=0;
  while(i<ret.length)
  {
      ans+=ret[i];
      i++;
  }
  return ans;
}