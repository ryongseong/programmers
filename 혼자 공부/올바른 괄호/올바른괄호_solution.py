def solution(s):
    answer = True

    string_list = []

    if s[0]==")":
        return False

    for elem in s:
        if elem == "(":
            string_list.append(elem)
        else:
            if not string_list:
                return False
            out = string_list.pop()
            if out == ")":
                return False
            
    if string_list:
        return False
    else :
        return True