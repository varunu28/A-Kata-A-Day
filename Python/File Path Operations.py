# File Path Operations
# Level: 6kyu
'''
This kata requires you to write an object that receives a file path and does operations on it. NOTE FOR PYTHON USERS: You cannot use modules os.path, glob, and re

Example of how the tests would work:

	>>> master = FileMaster('/Users/person1/Pictures/house.png')
	>>> master.extension()
	'png'
	>>> master.filename()
	'house'
	>>> master.dirpath()
	'/Users/person1/Pictures/'
'''

class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        return self.filepath[self.filepath.index('.')+1:]
    def filename(self):
        l = self.filepath[:self.filepath.index('.')]
        l_arr = l.split('/')
        return l_arr[-1]
    def dirpath(self):
        #Your code here
        l = self.filepath[:self.filepath.index('.')]
        l_arr = l.split('/')
        return '/'.join(l_arr[:len(l_arr)-1])+ '/'

# Test Case

master = FileMaster('/Users/person1/Pictures/house.png')
print(master.extension())
print(master.filename())
print(master.dirpath())