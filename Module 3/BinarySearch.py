class Solution:
    def binarysearch(self, list, k):
        self.index = k
        self.list = list
        for x in range(0,len(self.list)):
            try:
                if(self.index==self.list[x]):
                    print(f"{self.index} appears at index {self.list[x]}.")
                    break
                elif(self.index > self.list[self.index]):
                    raise IndexError
                else:
                    x+=x
            except IndexError:
                print(f"{self.index} is not present")
                break

arr1= [1, 2, 3, 4, 5]
k1 = 4   

arr2 = [11, 22, 33, 44, 55]
k2 = 445

arr3 = [1, 1, 1, 1, 2]
k3 = 1

S1 = Solution()
S2 = Solution()
S3 = Solution()

S1.binarysearch(list=arr1,k=k1)
S1.binarysearch(list=arr2,k=k2)
S1.binarysearch(list=arr3,k=k3)