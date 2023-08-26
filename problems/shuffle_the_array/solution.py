class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        right=0
        left=n
        array=[]
        while right<n:
            array.append(nums[right])
            array.append(nums[left])
            right+=1
            left+=1
        return array    
