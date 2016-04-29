//Count consonants
//Level: 7kyu
/*
Problem Description: Write a function consonantCount, consonant_count or ConsonantCount that takes a string of English
-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.
*/

function consonantCount(str) {
    str=str.toLowerCase();
    var vow='aeiou';
    var cons='abcdefghijklmnopqrstuvwxyz';
    var i=0;
    var n=0;
    
    while(i<str.length)
    {
      if(cons.indexOf(str[i])!==-1 && vow.indexOf(str[i])===-1)
      {
        n++;
      }
      i++;
    }
    return n;
}