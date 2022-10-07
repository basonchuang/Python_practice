class Solution(object):
    def pivotIndex(self, nums):
        ans = 0
        left = 0
        right = 0

        for i in range(len(nums)):
            if i == 0:
                left = 0
                for j in range(i+1, len(nums)):
                    right += nums[j]
            elif i > 0 & i < len(nums):
                for j in range(i-1):
                    left += nums[j]
                for k in range(i+1, len(nums)):
                    right += nums[k]
            else:
                for j in range(i-1):
                    left += nums[j]
                right = 0
            if left == right:
                ans = i
        return ans


s = Solution()
ans = s.pivotIndex([1,7,3,6,5,6])
print(ans)