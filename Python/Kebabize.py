# Kebabize
# Level: 6kyu
'''
Problem Description: Modify the kebabize function so that it converts a camel case string into a 
kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes: - the returned string should only contain lowercase letters
'''

def kebabize(string):
    #your code here
    ans = ''
    for i in string:
    	if i.isalpha():
            if i.isupper():
                ans += '-' + i.lower()
            else:
                ans += i
    if len(ans) > 0:
    	return ans if ans[0]!='-' else ans[1:]
    else:
        return ''

# Test Cases

print(kebabize('myCamelCasedString'))
print(kebabize('myCamelHas3Humps'))
print(kebabize('SOS'))