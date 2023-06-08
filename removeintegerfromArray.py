class Solution:
    def removeElement(self, nums ,val):
        for i in reversed(nums):
            if i == val:
                id = nums.index(i)
                nums.pop(id)   
        print(nums)           
        return(len(nums))
    

s = Solution()
print(s.removeElement([0,1,2,2,3,0,4,2],2))
        