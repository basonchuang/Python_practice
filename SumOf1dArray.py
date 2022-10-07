class Solution(object):
    def runningSum(self, nums):
        ans = []
        for i in range(len(nums)):
            tmp = 0
            for j in range(i+1):
                if i == 0:
                    tmp = nums[i]
                else:
                    tmp += nums[j]
            ans.append(tmp)
        return ans

s = Solution()
ans = s.runningSum([1,2,3,4])
print(ans)