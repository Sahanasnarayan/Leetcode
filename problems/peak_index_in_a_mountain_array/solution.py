class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        while left<=right:
            m=(left+right)//2
            if arr[m+1] < arr[m] and arr[m-1] < arr[m]: return m
            if arr[m+1] > arr[m]: left = m+1
            else: right = m