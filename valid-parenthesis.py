class Solution(object):
    def isValid(self, s) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = {'(', '{', '['}
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop() != mapping[ch]:
                    return False

        return not stack
