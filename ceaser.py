'''
a= input('Enter your message: ')
coded= ''
for b in a:
    if not b.isalpha():
        continue
    b= b.upper()
    code= ord(b)+ 1
    if code > ord('Z'):
        code=ord('A')
    coded+= chr(code)
print(coded)

original=''
for r in coded:
    if not r.isalpha():
        continue
    r= r.upper()
    dec= ord(r)-1
    if dec< ord('A'):
        dec= ord('Z')
    original+= chr(dec)
print(original)
'''
class A:
    def a(self, v= 1):
        self.__a= v

t= A()
t.a(0)
print(len('\\\\'))