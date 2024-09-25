def is_correct_bracket_seq(check_string):
    if not len(check_string):
        return True
    if len(check_string) % 2:
        return False
    etalon = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []
    for i in check_string:
        if i in etalon.values():
            stack.append(i)
            print(stack)
            continue
        print(etalon[i])
        if len(stack) and etalon[i] == stack[-1]:    
            stack.pop()
            print(stack)
            continue
        return False
    if not len(stack):
        return True
    return False


check_string = input()
print(is_correct_bracket_seq(check_string))