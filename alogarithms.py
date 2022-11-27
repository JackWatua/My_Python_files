class alogs:
    def linear_search(self, list, target):
        for i in range(0, len(list)):
            if list[i]== target:
                return i
        return None
    def verify(self, index):
        if index is not None:
            print('Target found at index', index)
        else:
            print('Item not found in the list!!')

numbers=[a+1 for a in range(10)]
a= alogs()

f= a.linear_search(numbers,10)
r= a.linear_search(numbers,1)
a.verify(f)
a.verify(r)
'''
The above code is a linear serch alogarthim that searches for a targeted element starting from the first index towards
the last index. The code below is a binary serach alogarithim that searches the targeted element by dividing the list into
half and gets rid of part of the list outside the targeted range. the operation repeats itself until the 
specified target is found. With binary search, the list has to be sorted because we deppend on comparison,
'''
def binary_search(list, target):
    first=0
    last= len(list)-1
    while first<= last:
        midpoint= (first+last)//2
        if list[midpoint]== target:
            return midpoint
        elif list[midpoint] < target:
            first= midpoint + 1
        else:
            last= midpoint -1
    return None

p= binary_search(numbers, 10)
b= binary_search(numbers, 1)
def verify(index):
    if index is not None:
        print('Target found at index', index)
    else:
        print('Item not found in the list!!')

''''
Recursive binary search
'''
def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    else:
        midpoint= len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint]< target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

numbers=[i+1 for i in range(10)]
print(numbers[:5])