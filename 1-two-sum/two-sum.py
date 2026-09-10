class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # 1. Iterate over every possible number pair
        for i in range(len(nums)):
            # j is always ahead of i so that we don't re-evaluate already evaluated sums
            for j in range(i+1, len(nums)):
                # 2. Check if a given pair adds up to our target
                if nums[i] + nums[j] == target:
                    # Return the indices when a pair has been found
                    return i, j        