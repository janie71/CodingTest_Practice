def solution(s):
    answer = True
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        elif i==")":
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False

    return True