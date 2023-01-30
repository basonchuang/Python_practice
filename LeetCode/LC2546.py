class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        def containOne(s):
            for ch in s:
                if (ch == '1'): return True
            return False
        if s == target: return True
        return containOne(s) & containOne(target)
s = '1010'
target = '0110'

sol = Solution()
print(sol.makeStringsEqual(s, target))

'''
(0,0) -> (0,0)
(0,1) -> (1,1)
(1,0) -> (1,1)
(1,1) -> (1,0)

s: 1 X X X
t: 1 X X X

s: 1 X X X
t: 0 (X X X) contain 1
'''