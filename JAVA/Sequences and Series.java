// Sequences and Series
// Level : 6kyu
/*
Have a look at the following numbers.

 n | score
---+-------
 1 |  50
 2 |  150
 3 |  300
 4 |  500
 5 |  750
Can you find a pattern in it? If so, then write a function getScore(n)/get_score(n)/GetScore(n) which returns the score for any positive number n:

*/

public class Sequence {

  public static long getScore(long n) {
    // do your magic here
    
    int i = 1;
    long sum = 0;
    while (i <= n) {
      sum += i;
      i++;
    }
    
    return 50*sum;
  }
}
