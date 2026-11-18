class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevnums = set()
        for x in nums: 
            if x in prevnums:
                return True
            prevnums.add(x)
        
        return False