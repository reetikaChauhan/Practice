class Solution:
    def maxSubArray(self, nums):
        temp=0
        sum = nums[0]
        for i in nums:
            print('i',i)
            temp = temp+i
            print('temp',temp)
            if (temp>sum):
                sum= temp   
            if (temp < 0):
                temp=0
        return sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        