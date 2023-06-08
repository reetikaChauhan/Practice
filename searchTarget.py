class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return(nums.index(target))
        else:
            for i in range(len(nums)):
                if nums[i]> target:
                    return i
            return len(nums)

s = Solution()
print(s.searchInsert([1,4,6,7],7))

# O(log(n))
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1
#         while left <=right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid]<target:
#                 left = left+1
#             else:
#                 right = right -1
#         return left