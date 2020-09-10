package kata

/*
In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space at index 3, so the string becomes "edo cruo"

solve("your code rocks") = "skco redo cruoy". 
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.
*/

import "unicode"

// Solve : Reverse string
func Solve(s string) string {
  r := []rune(s)
  start := 0
  end := len(s) - 1
  for start < end {
    if !unicode.IsSpace(r[start]) && !unicode.IsSpace(r[end]) {
      temp := r[start]
      r[start] = r[end]
      r[end] = temp
      start++
      end--
    } else if unicode.IsSpace(r[start]) {
      start++
    } else {
      end--
    }
  }
  return string(r)
}
