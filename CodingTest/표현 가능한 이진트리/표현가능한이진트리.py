from math import log


def check(binary_number, prev_parent):
    mid = len(binary_number) // 2
    if binary_number:
        child = (binary_number[mid]) == "1"
    else:
        return True

    if child and not prev_parent:
        return False
    else:
        return check(binary_number[mid + 1 :], child) and check(
            binary_number[:mid], child
        )


def sol(number):
    if number == 1:
        return 1
    binary_number = bin(number)[2:]
    digits = 2 ** (int(log(len(binary_number), 2)) + 1) - 1
    binary_number = "0" * (digits - len(binary_number)) + binary_number

    return (
        1
        if binary_number[len(binary_number) // 2] == "1" and check(binary_number, True)
        else 0
    )


def solution(numbers):
    answer = []

    for num in numbers:
        answer.append(sol(num))

    return answer


print(solution([7, 42, 5]))  # [1, 1, 0]
print(solution([63, 111, 95]))  # [1, 1, 0]
