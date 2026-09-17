class Solution:
    def isValid(self, s: str) -> bool:
        pts = {"(":")", "[":"]", "{":"}"}
        stack = []
        for char in s:
            if char in pts.keys():
                stack.append(char)
                continue
            elif char in pts.values():
                if not stack:
                    return False
                popped = stack.pop()
                if pts[popped] == char:
                    continue
                else:
                    return False
        if not stack:
            return True
        return False

