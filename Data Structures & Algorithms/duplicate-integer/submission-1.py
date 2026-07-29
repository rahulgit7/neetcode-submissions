class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        # hash_set = set()
        # for i in range(0, len(nums)):
        #     if nums[i] in hash_set:
        #         return True
        #     else:
        #         hash_set.add(nums[i])
        # return False
