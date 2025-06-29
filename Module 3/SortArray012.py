class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self,list):
         a = list
         for x in range(0,len(a)):
            for y in range(x+1,len(a)):
                if(a[x] > a[y]):
                    temp = a[x]
                    a[x] = a[y]
                    a[y] = temp
         print(f"0s, 1s, and 2s are segregated into ascending order.")
         print(f"List contents after sorting: {a}")    

arr1 = [0, 2, 1, 0, 2, 1]
arr2 = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

S1 = Solution()
S2 = Solution()

arr1 = Solution.sort012(S1,arr1)
arr2 = Solution.sort012(S2,arr2)
