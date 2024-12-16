class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) == 0:
                    return False
                # if the brackets are not matching then return false
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif i == "{":
                stack.append(i)
            elif i == "}":
                if len(stack) == 0:
                    return False
                # if the brackets are not matching then return false
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            
            elif i == "[":
                stack.append(i)
            elif i == "]":
                if len(stack) == 0:
                    return False
                # if the brackets are not matching then return false
                if stack[-1] == "[":
                        stack.pop()
                else:
                    return False
            
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False





sol = Solution()
sol.isValid("(]")
