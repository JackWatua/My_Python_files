class a:
    var= 'L'
    left= 'LL'
    right= 'KK'
    def fun(self):
        return 'Left'
    def names(self):
        self.names= ['Jack', 'Watua', 'Wanyoynyi', 'Benjamin']
class b:
    var= 'M'
    right= 'RR'
    def fun(self):
        return 'Right' 
class c(b,a):
    pass

g= c()
print(g.var, g.left, g.right, g.fun())


