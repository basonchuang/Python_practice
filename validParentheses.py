class Solution(object):
    def f(x):
        return {
            'a': 1,
            'b': 2,
        }[x]
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n_of_condition = []
        if "(" in s:
            left = s.index("(")
            right = s.find(")")
            if right == -1:
                n_of_condition.append(False)
            elif right == left + 1:
                n_of_condition.append(True)
            elif (right - left) % 2 == 1:
                n_of_condition.append(True)
            else:
                n_of_condition.append(False)
        if "[" in s:
            left = s.index("[")
            right = s.find("]")
            if right == -1:
                n_of_condition.append(False)
            elif right == left + 1:
                n_of_condition.append(True)
            elif (right - left) % 2 == 1:
                n_of_condition.append(True)
            else:
                n_of_condition.append(False)
        if "{" in s:
            left = s.index("{")
            right = s.find("}")
            if right == -1:
                n_of_condition.append(False)
            elif right == left + 1:
                n_of_condition.append(True)
            elif (right - left) % 2 == 1:
                n_of_condition.append(True)
            else:
                n_of_condition.append(False)

        count = 0
        for i in n_of_condition:
            if i:
                count+=1
        if count != 0 and count == len(n_of_condition):
            return True
        else:
            return False
sol = Solution()
ans = sol.isValid("(){}}{")
print(ans)