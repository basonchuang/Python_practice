class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, match = [], {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in match:
                if not (stack and stack.pop() == match[char]):
                    return False
                else:
                    stack.append(char)
        return not stack