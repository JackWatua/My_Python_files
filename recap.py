class searches:
    def linear_search(self, list, target):
        for i in range(0, len(list)):
            if list[i]== target:
                return i
        return None
    def verify_result(self, result):
        if result != None:
            print('item found at index, ', result)
        else:
            print('Item not found in the list!')
    def binary_search(self, list, target):
        self.start = 0
        self.stop = len(list) - 1         
        while self.start <= self.stop:
            self.midpoint= (self.start + self.stop)//2
            if list[self.midpoint]==target:
                return self.midpoint
            elif list[self.midpoint] < target:
                self.start = self.midpoint + 1
            else:
                self.stop = self.stop -1  
        return None
    def recursive_binary_search(self, list, target):  
        if len(list) == 0:
            return False
        else:
            self.midpoint = len(list)//2
            if list[self.midpoint] == target :
                return True
            elif list[self.midpoint] < target :
                return self.recursive_binary_search(list[self.midpoint+1:], target)
            else:
                return self.recursive_binary_search(list[:self.midpoint], target)
    def verify_recursive(self, result):
        print('Target Found: ', result)