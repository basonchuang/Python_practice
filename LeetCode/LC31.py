class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lp = len(nums) - 1
        while(lp>0 and nums[lp-1]>=nums[lp]):
            lp -= 1
        if lp > 0:
            start = lp
            end = len(nums) - 1

            while start <= end:
                mid = (start + end) // 2
                if nums[mid] <= nums[lp-1]:
                    end = mid -1
                else:
                    start = mid + 1
            nums[end], nums[lp-1] = nums[lp-1], nums[end]
        rp = len(nums) - 1
        while(lp < rp):
            nums[lp], nums[rp] = nums[rp], nums[lp]
            lp+=1
            rp-=1