class Solution:
    def maxSubArray(self, nums):
        if len(nums)>1:
            mid = len(nums)//2
            left_list = nums[:mid]
            right_list = nums[mid:]
            self.maxSubArray(left_list)
            self.maxSubArray(right_list)
            temp1=0
            temp2=0
            print('left_list',left_list)
            print('right_list',right_list)
            for i in range(len(left_list)):
                temp1 = temp1+left_list[i]
            for j in range(len(right_list)):
                temp2= temp2+right_list[j]
            if temp1>temp2:
                sum.append(temp1)
                sum.sort()
            else:
                sum.append(temp2)
                sum.sort()
        return sum
            


    
    

     

s = Solution()
sum=[]
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))