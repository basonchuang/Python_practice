class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, match = [], {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char not in match:
                stack.append(char)
            else:
                if not stack or stack.pop() != match[char]:
                    return False
        return not stack

s = "()"

sol = Solution()
print(sol.isValid(s))