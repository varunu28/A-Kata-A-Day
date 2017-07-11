// Find divisors number
// Level: 7kyu
/*
Find the number of divisors of a positive integer n.

Example:

divisors 4  = 3 -- 1, 2, 4
divisors 5  = 2 -- 1, 5
divisors 12 = 6 -- 1, 2, 3, 4, 6, 12
divisors 30 = 8 -- 1, 2, 3, 5, 6, 10, 15, 30
*/

public class FindDivisor {

  public long numberOfDivisors(int n) {
    // TODO please write your code below this comment
    int i=1;
    int count=0;
    while (i<=n) {
      if (n%i == 0) {
        count++;
      }
      i++;
    }
    return count;
  }
}
