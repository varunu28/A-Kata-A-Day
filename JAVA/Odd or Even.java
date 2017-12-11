// Odd or even
// Level: 7kyu
/*
Given an array of numbers, determine whether the sum of all of the numbers is odd or even.

Give your answer in string format as 'odd' or 'even'.

If the input array is empty consider it as: [0] (array with a zero).
*/

public class Codewars {
  public static String oddOrEven (int[] array) {
    int sum = 0;
    for (int i=0;i<array.length;i++) {
      sum += array[i];
    }
    
    return sum%2 == 0 ? "even" : "odd";
  }
}
