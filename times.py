from time import time, ctime
t= time()
print('This program keeps track of your typing speed')
a= input('Type a sentence press enter to stop and know the results: ')
b= a.split()
duartion= time()-t
print('You typed', len(b), '  words in ',duartion,' seconds')
