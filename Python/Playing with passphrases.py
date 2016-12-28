# Playing with passphrases
# Level: 6kyu
'''
Problem Description: Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

    shift each letter by a given number but the transformed letter must be a letter (circular shift),
    replace each digit by its complement to 9,
    keep such as non alphabetic and non digit characters,
    downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
    reverse the whole result.

Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?
'''


def play_pass(s, m):
    i = 0
    ans = []
    while i < len(s):
        if s[i].isnumeric():
            ans.append(str(abs(int(s[i]) - 9)))
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            n = ord(s[i]) + m
            if n > 90:
                n = (n-90) + 64

            if (i) % 2 == 0:
                ans.append(chr(n).upper())
            else:
                ans.append(chr(n).lower())
        else:
            ans.append(s[i])
        i += 1
    return ''.join(ans)[::-1]

# Test Case

print(play_pass("I LOVE YOU!!!", 1))
print(play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2))
