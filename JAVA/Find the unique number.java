// Find the unique number
// Level: 6kyu
/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

Kata.findUniq(new double[]{ 1, 1, 1, 2, 1, 1 }); // => 2
Kata.findUniq(new double[]{ 0, 0, 0.55, 0, 0 }); // => 0.55
It’s guaranteed that array contains more than 3 numbers.
*/
// Make sure your class is public
import java.util.Arrays;

 public class Kata {
    public static double findUniq(double arr[]) {
      // Do the magic
      Arrays.sort(arr);
      if (arr[0] == arr[1]) {
        return arr[arr.length-1];
      }
      return arr[0];
    }
}