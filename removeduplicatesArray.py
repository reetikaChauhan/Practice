class Solution:
    def removeDuplicates(self, nums) :
        k = 0
        temp = nums[0]
        j=1
        while  j<len(nums) and nums[j]!= 1000:
            if temp == nums[j]:
                k = k+1
                nums[j]=1000
                nums.sort()
                print('if',nums)
            else:
                temp=nums[j]
                j=j+1 
                print('else',nums)
        k = len(nums)-k
        del nums[k:]
        print(nums)
        return k

s = Solution()
print(s.removeDuplicates([1,2,3,4]))