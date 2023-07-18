class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        seen = set()
        for num in a:
            if num in seen:
                return True
            seen.add(num)
        return False
           