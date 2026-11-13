
# This is the code for the quick short
#-----------------------------------------------------
class Solution(object):
    def partition(self,arr,low,high):
        i,j=low+1,high 
        pivot = arr[low]

        while i<=j:
            while i<=high and arr[i]<=pivot:
                i+=1
            while j>low and arr[j]>pivot:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[low],arr[j] = arr[j],arr[low]
        return j
    def quickSort(self,arr,low,high):
        if low<high:
            pivot_index = self.partition(arr,low,high)
            self.quickSort(arr,low,pivot_index-1)
            self.quickSort(arr,pivot_index+1,high)
t1=Solution()
arr=[1,2,3,4,5]
t1.quickSort(arr,0,len(arr)-1)
print(arr)


# ---------------------------------------------------------
# QUICK SORT: TIME AND SPACE COMPLEXITY ANALYSIS
# ---------------------------------------------------------

# TIME COMPLEXITY:
#
# 1. Best Case: O(n log n)
#    - Occurs when the pivot divides the array into two
#      nearly equal subarrays at every partition.
#    - The recursion depth is log(n), and each level
#      requires O(n) partitioning work.
#
# 2. Average Case: O(n log n)
#    - Occurs when partitions are reasonably balanced
#      on average.
#    - The algorithm performs approximately log(n) levels
#      of recursion, with O(n) work at each level.
#
# 3. Worst Case: O(n^2)
#    - Occurs when the pivot is always the smallest or
#      largest element.
#    - One partition contains n-1 elements, while the
#      other partition is empty.
#    - Comparisons: (n-1) + (n-2) + ... + 1.
#
# SPACE COMPLEXITY (Auxiliary Space):
#
# 1. Best Case: O(log n)
#    - Balanced partitions produce a recursion depth
#      of approximately log(n).
#
# 2. Average Case: O(log n)
#    - The recursion stack requires logarithmic space
#      on average.
#
# 3. Worst Case: O(n)
#    - Highly unbalanced partitions produce a recursion
#      depth of approximately n.
#
# note:
# - In-place partitioning requires O(1) auxiliary space
#   per partition operation.
# - The recursion stack determines the overall
#   auxiliary space complexity.
#
# ---------------------------------------------------------
