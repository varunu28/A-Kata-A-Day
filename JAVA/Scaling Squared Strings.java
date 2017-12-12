// Scaling Squared Strings
// Level: 7kyu
/*
You are given a string of n lines, each substring being n characters long. For example:

s = "abcd\nefgh\nijkl\nmnop"

We will study the "horizontal" and the "vertical" scaling of this square of strings.

A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').

Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
A v-vertical scaling of a string consists of replicating v times each part of the squared string.

Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.

Example: a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3) --> 
"aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
*/

public class Scale {
    
    public static String scale(String strng, int k, int v) {
        // your code
        String[] str = strng.split("\n");
        String ans = "";
        
        for (String s : str) {
          String temp = "";
          String[] tempArr = s.split("");
          
          for (String t : tempArr) {
            for(int i = 1;i <= k; i++) {
              temp = temp + t;
            }
          }
          
          for(int i = 1;i <= v; i++) {
            ans = ans + temp + "\n";
          }
          
        }
        
        return ans.trim();
    }
}
