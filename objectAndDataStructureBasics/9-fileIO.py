# This exercise will require several lines of code.
# Write a script that opens a file name 'test.txt', writes 'Hello World' to the file, then closes it.

with open('test.txt', mode='w') as myfile:
    myfile.write('Hello World')