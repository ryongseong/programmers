def solution(s):
    answer = True

    string_list = []
    for i in s:
        string_list.append(i)
 
    if string_list.count('(') != string_list.count(')'):
        answer = False

    if answer == True:
        if string_list[0] == ')' or string_list[-1] == '(':
            answer = False

    return answer

print(solution('((()()'))