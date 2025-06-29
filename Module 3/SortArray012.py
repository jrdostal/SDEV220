import array as arr

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        self.arr = arr
        a = self.arr
        for x in range(0,len(a)):
            for y in range(x+1,len(a)):
                if(a[x] > a[y]):
                    temp = a[x]
                    a[x] = a[y]
                    a[y] = temp
                    
        print(f"0s, 1s, and 2s are segregated into ascending order.")
    
    def size(self, arr):
        self.size = arr
        if(len(self.size) == (1 <= self.size <= 10**6)):
            pass
        else:
            print(f"{self} does not meet the size constraints for an array.")
    
    def values(self, arr):
        self.values = arr
        a = self.values
        for x in range(0,len(a)):
            if(a[x] == (0 <= a[x] <= 2)):
                pass
            else:
                print(f"{self} contains a value that does not meet that value constraints for an array.")
                
    def __init__(self, arr):
        Solution.size(arr)
        Solution.values(arr)
        Solution.sort012(arr)
        print(f"Array {self} successfully created and sorted!")

arr1 = arr.array("i",[0, 1, 2, 0, 1, 2])
arr2 = arr.array("i",[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])