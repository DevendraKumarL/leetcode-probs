/*
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

    Solution: (Fast?)
        -maintain a hashmap <char, char> for } => { ..
        -have a stack to push char from s if is one of ['{', '[', '(']
        -if the char is closing parentheses then check the top of stack should have the corresponding opening parentheses
        -reurn true if stack is empty at the end or if the stack size is 0 in empty the loop
*/

class Solution {
public:
    bool isValid(string s) {
        map<char, char> parentheses = {
            {')', '('}, {'}', '{'}, {']', '['}
        };
        vector<int> stack;
        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (c == '(' || c == '{' || c == '[') {
                stack.push_back(c);
            } else if (stack.size() > 0 && parentheses[c] == stack.back()) {
                stack.pop_back();
            } else {
                return false;
            }
        }
        return stack.size() == 0;
    }
};