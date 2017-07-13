// Money, Money, Money
// Level: 7kyu
/*
Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' this sum has to be kept in the bank in order for this sum of money to amount to 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, and the new sum is re-invested yearly after paying tax 'T'

Note that the principal is not taxed but only the year's accrued interest
*/

public class Money {
  public static int calculateYears(double principal, double interest,  double tax, double desired) {
    // your code
    int count = 0;
    while (principal < desired) {
      double i = principal*interest;
      i -= i*tax;
      principal += i;
      count++;
    }
    return count;
  }
}