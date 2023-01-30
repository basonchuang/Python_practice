class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        temp = []
        for i in range(len(weights)-1):
            temp.append(weights[i]+weights[i+1])
        temp.sort()
        diff = 0
        for i in range(k-1):
            diff += temp[len(temp)-1-i]
        for i in range(k-1):
            diff -= temp[i]
        return diff

weight = [8, 13, 11, 7]
k = 3

s = Solution()
print("Result: ", s.putMarbles(weight, k))