package kata

/*
For a given string s find the character c (or C) with longest consecutive repetition and return:

type Result struct {
    C rune // character
    L int  // count
}
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:
*/

// Result result
type Result struct {
	C rune // character
	L int  // count
}

// LongestRepetition : function to get longest repeating character
func LongestRepetition(text string) Result {
	if len(text) == 0 {
		return Result{}
	}
	r := []rune(text)
	i := 0
	maxCount := 0
	maxCountRune := r[0]
	for i < len(r) {
		currRune := r[i]
		currCount := 0
		for i < len(r) && r[i] == currRune {
			i++
			currCount++
		}
		if maxCount < currCount {
			maxCount = currCount
			maxCountRune = currRune
		}
	}
	return Result{
		C: maxCountRune,
		L: maxCount,
	}
}
