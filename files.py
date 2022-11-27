'''
#To open a file, we use open() and close. Open can take 2 or even 3 arguements. to close a stream we use close()
#Modes
rt- read text           rd          Requires the file to exist
rw- write               rd          Does not require the file to exist. If a file doesn't exist a new file will be created
at- append text         ad          Does not require the file to exist. Adds tex, or item or content at the end of an existing one
r+t- read and update    r+d         The file Must exist
w+t- write and update   w+d         Does not necessarily reauire the file to exist
SYNTAX:
        stream= open(file, mode, encryption)
        stream.close

from os import strerror


try:
        ccnt=lcnt=0
        s= open("C:\\Users\\Jack Watua\\Desktop\\Watua\\JB_WORLD\\files.txt", "rt")
        d= s.readlines()
        while d != '':
                lcnt+=1 
                for t in d:
                        print(t, end='')
                        ccnt+=1
                d= s.readlines()
        s.close()
        print('\n\nLines',lcnt)
        print('Total characters', ccnt)
except Exception as er:
        print(strerror(er.errno))
'''
s= open("C:\\Users\\Jack Watua\\Desktop\\Watua\\JB_WORLD\\files.txt", "rd")
f= ''''2. Project communication and negotiation
3. Project Control
4. Project Quality
5. Project Monitoring
6. Project risk management
7. Project teams
'''