class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bot = 0
        top = len(nums)
        while (top - bot) > 0:
            mid = (top+bot)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                bot = mid+1
            elif target < nums[mid]:
                top = mid
        return -1                

        