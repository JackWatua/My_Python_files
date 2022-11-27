class search:
    def linear_search(self, list, target):
        for i in range(0, len(list)):
            if list[i]==target:
                return i
        return None

    def binary_search(self, list, target):
        first= 0
        last= len(list)  - 1
        while first <= last:
            midpoint=(first + last) // 2
            if list[midpoint]== target:
                return midpoint
            elif list[midpoint] < target:
                first= midpoint+1
            else:
                last= midpoint-1
        return None

    def recursive_binay_search(self, list, target):
        if len(list) == 0:
            return False
        else:
            midpoint= len(list) // 2
            if list [midpoint] == target :
                return True
            else:
                if list [midpoint] < target :
                    return self.recursive_binay_search (list[midpoint + 1: ], target)
                else:
                    return self.recursive_binay_search (list[:midpoint], target) 
