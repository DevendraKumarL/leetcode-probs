'''
    Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    Example 1:
    Input: s = "()[]{}"
    Output: true

    Example 2:
    Input: s = "(]"
    Output: false

    Solution1: (Slow)
        -maintain a stack to store the chars in the given str
        -push if a char is [ "(", "{", "[" ]
        -pop if char is [ ")", "}", "]" ] and the top of stack is the corresponding opening bracket
        -return true is stack is empty

    Solution2: (Fast?)
        -similar to the above
        -instead of checking the char with if else.. use a hashmap
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        for s1 in s:
            if s1 in ["(", "{", "["]:
                stack.append(s1)
                top += 1
            else :
                if len(stack) == 0:
                    return False
                elif s1 == ")" and stack[top] == "(":
                    stack = stack[:top]
                    top -= 1
                elif s1 == "]" and stack[top] == "[":
                    stack = stack[:top]
                    top -= 1
                elif s1 == "}" and stack[top] == "{":
                    stack = stack[:top]
                    top -= 1
                else:
                    return False
        return top == -1

# OR

class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []