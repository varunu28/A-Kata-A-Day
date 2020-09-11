package kata

import "unicode"

func solve(str string) string {
	lowerCount := 0
	upperCount := 0
	for _, c := range str {
		if unicode.IsUpper(c) {
			upperCount++
		} else {
			lowerCount++
		}
	}
	makeUpper := upperCount > lowerCount
	r := []rune(str)
	for i, rn := range r {
		if makeUpper && unicode.IsLower(rn) {
			r[i] = unicode.ToUpper(rn)
		} else if !makeUpper && unicode.IsUpper(rn) {
			r[i] = unicode.ToLower(rn)
		}
	}
	return string(r)
}
