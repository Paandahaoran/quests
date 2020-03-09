class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        lvp = []
        for item in s:
            if item == "(" and len(lvp) == 0:
                lvp.append(item)
            if item != lvp[-1] and len(lvp)!= 0:
                lvp.append(item)
            print(lvp)
        print(len(lvp))
        return len(lvp)




Solution().longestValidParentheses("(()())()()")
