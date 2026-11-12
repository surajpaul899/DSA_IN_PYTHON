# This is the code for the merge short:
class Solution(object):
    @staticmethod
    def merge_arr(left,right):
        result=[]
        i,j=0,0
        n,m = len(left),len(right)

        while i<n and j<m:
            if left[i] <= right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1

        if i<n:
            while i<n:
                result.append(left[i])
                i+=1
        if j<m:
            while j<m:
                result.append(right[j])
                j+=1
        return result

    @staticmethod
    def merge_sort(arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left = Solution.merge_sort(left_arr)
        right = Solution.merge_sort(right_arr)
        return Solution.merge_arr(left,right)

m1 = Solution()
print(m1.merge_sort([5,1,3,8,0,9,6,2,4]))
        
        
        