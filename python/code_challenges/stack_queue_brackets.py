from inspect import stack
from data_structures.stack import Stack


def multi_bracket_validation(string):
    """ Returns True if all brackest are matched """
    d = {'{':'}', '[':']', '(':')'}
    stack = Stack()

    for ch in string:
        if ch in d.keys():
            stack.push(ch)
        elif ch in d.values():
            if stack.is_empty():
                return False
            elif d[stack.peek()] == ch:
                stack.pop()
            else:
                return False

    if stack.is_empty():
        return True
    else:
        return False
