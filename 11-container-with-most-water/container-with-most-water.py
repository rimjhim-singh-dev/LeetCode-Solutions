class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_water = 0, len(height) - 1, 0
        while left < right:
            max_water = max(max_water, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: 
                left+= 1
            else:
                right -= 1
        return max_water