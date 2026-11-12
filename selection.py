# The code for Selection Sort
class Solution(object):
    def selectionsort(self,arr):
        for i in range(len(arr)-1):
            min_idx = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_idx]:
                    min_idx = j
                else:
                    continue
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
        return arr
t = Solution()
print(t.selectionsort([8,3,5,1,2,8,4,6]))
# time complexity is o(n(n+1)/2) = o(n^2)
# space complexity is o(1) as it is fixed
