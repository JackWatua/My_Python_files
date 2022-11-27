class A:
        Insts = 0
        def __init__(self, message = "from Parent",cls = "A"):
                self.message = message
                A.Insts += 1
                if __name__  == "__main__":
                        print(self.PrintSelf())

        def PrintSelf(self) -> str:
                return f"Object {self.message}"
        
        def pass_test(self, val):
                pass

class B(A):
        def __init__(self, message="from Child B", cls = "B"):
            super().__init__(message , cls = cls)
        
        def have_fun(self, location = "B"):
                self.location = location
                return 'having  fun from {}'.format(location)

class C(A):
        def __init__(self, message="from Child C", cls = "C"):
            super().__init__(message , cls = cls)
            self.Code = 1231
        
        def have_fun(self, location = "C"):
                self.location = location
                return 'having  fun from {}'.format(location)

class D(C, B):
        def __init__(self, message="from Child D", cls = "D"):
            super().__init__(message , cls = cls)
        def have_fun(self, location = "Self"):
                self.location = location
                return 'having  fun from {}'.format(location)
        def pass_test(self, val):
                if val % 2  == 0:
                        self.test = "Pass"
                        return self.test
                else:
                        self.alert = "Test failed"
                        return self.alert


v = A()
c = B ()
d = D()