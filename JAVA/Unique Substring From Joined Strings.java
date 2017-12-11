// Unique Substring From Joined Strings
// Level: 6kyu
/*
Write a function that takes two strings, A and B, and returns the length of the longest possible substring that can be formed from either the concatenation A + B or B + A containing only characters that do not appear in both A and B.

Example:

Given the strings "piquancy" and "refocusing":
A = "piquancy"
B = "refocusing"
A + B = "piquancyrefocusing"
B + A = "refocusingpiquancy"

Since 'i', 'n', 'u', and 'c' appear in both A and B, all acceptable substrings without those characters are:
"p", "q", "a", "yrefo", "s", "g" (from A + B)
"refo", "s", "gp", "q", "a", "y" (from B + A)

Therefore, it would be correct to return 5: the length of "yrefo".
*/

import java.util.*;
public class FindSubstring {
  static int longestSubstring(String a, String b){
    
    String s1 = a+b;
    String s2 = b+a;
    
    Set<String> set = new HashSet<>();
    String temp = "";
    
    for (int i=0;i<s1.length();i++) {
      if (a.indexOf(s1.charAt(i)) != -1 && b.indexOf(s1.charAt(i)) != -1) {
        if (temp.length() > 0) {
          set.add(temp);
          temp = "";
        }
      }
      else {
        temp = temp + String.valueOf(s1.charAt(i));
      }
    }
    
    if (temp.length() > 0) set.add(temp);
    
    temp = "";
    
    for (int i=0;i<s2.length();i++) {
      if (a.indexOf(s2.charAt(i)) != -1 && b.indexOf(s2.charAt(i)) != -1) {
        if (temp.length() > 0) {
          set.add(temp);
          temp = "";
        }
      }
      else {
        temp = temp + String.valueOf(s2.charAt(i));
      }
    }
    
    if (temp.length() > 0) set.add(temp);
    
    int maxL = 0;
    
    for (String s : set) {
        
        maxL = Math.max(maxL,s.length());
    }
    return maxL;
  }
}
