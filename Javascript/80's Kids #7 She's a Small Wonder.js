//80's Kids #7: She's a Small Wonder
//Level:6kyu
/*
Problem Description: Vicky is quite the small wonder. Most people don't even realize she's not a real girl, but a 
robot living amongst us. Sure, if you stick around her home for a while you might see her creator open up her back 
and make a few tweaks and even see her recharge in the closet instead of sleeping in a bed.

In this kata, we're going to help Vicky keep track of the words she's learning.

Write a function, learnWord(word) which is a method of the Robot object. The function should report back whether the
word is now stored, or if she already knew the word.

Example:

var vicky = new Robot();
vicky.learnWord('hello') -> 'Thank you for teaching me hello'
vicky.learnWord('abc') -> 'Thank you for teaching me abc'
vicky.learnWord('hello') -> 'I already know the word hello'
vicky.learnWord('wow!') -> 'I do not understand the input'
Case shouldn't matter. Only alpha characters are valid. There's also a little trick here. Enjoy!
*/

function Robot() {
  this.ans = []; 
}

Robot.prototype.learnWord = function(word) 
{
  var res;
  var word_arr=word.split(" ");
  if(word_arr.length===1 && word!=='')
  {
      var lower_word=word.toLowerCase();
      var knowledge=('thank you for teaching me i already know the word do not understand the input').split(" ");
      
      if(/^[a-zA-Z- ]*$/.test(lower_word) === true)
      {
          if(this.ans.indexOf(lower_word)===-1 && knowledge.indexOf(lower_word)===-1)
          {
              
              this.ans.push(lower_word);
              res = 'Thank you for teaching me '.concat(word);
              return res;
          }
          else
          {
              res = 'I already know the word '.concat(word);
              return res;
          }
      }
      else
      {
          res='I do not understand the input';
          return res;
      }
  }
  else
  {
      res='I do not understand the input';
      return res;
  }
}

var vicky = new Robot();
