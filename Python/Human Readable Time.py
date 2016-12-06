# Human Readable Time
# Level: 5kyu
'''
Problem Description: Write a function, which takes a non-negative integer (seconds) as input and 
returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''

def make_readable(seconds):
	hr = 0
	m = 0
	sec = 0
	hr = seconds//3600
	seconds = seconds%3600
	m = seconds//60
	seconds = seconds%60
	sec = seconds

	return '{:02d}'.format(hr) + ':' + '{:02d}'.format(m) + ':' + '{:02d}'.format(sec) 

print(make_readable(60))