s = "(())()"


def is_correct_parenthesis(string):
    # 구현해보세요!
    stack = []
    for element in string:
        if element == "(":
            stack.append(element)
        elif element == ")":
            stack.pop()
    if not stack:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
