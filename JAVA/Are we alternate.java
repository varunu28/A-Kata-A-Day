// Are we alternate?
// Level: 6kyu
/*
Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

isAlt("amazon")
// true
isAlt("apple")
// false
isAlt("banana")
// true
Arguments consist of only lowercase letters.
*/

public class Solution {
    public static boolean isAlt(String word) {
        //make note that 'y' should not be treated as vowel
        //your code here
        String vowel = "aeiou";
        int vowelFlag = vowel.indexOf(word.charAt(0));
        for (int i=1;i<word.length();i++) {
            if ((vowelFlag>=0 && (vowel.indexOf(word.charAt(i)))>=0) || (vowelFlag<0 && (vowel.indexOf(word.charAt(i)))<0)){
                return false;
            }
            else {
                vowelFlag = vowel.indexOf(word.charAt(i));
            }
        }
        return true;
    }
}