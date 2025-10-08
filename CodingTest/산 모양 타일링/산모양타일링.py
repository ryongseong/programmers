MOD = 10007


def solution(n, tops):
    dp1, dp2 = [0] * n, [0] * n
    dp1[0] = 1
    dp2[0] = 2 + tops[0]

    for i in range(1, n):
        dp1[i] = (dp1[i - 1] + dp2[i - 1]) % MOD
        dp2[i] = ((dp1[i - 1] * (1 + tops[i])) + dp2[i - 1] * (2 + tops[i])) % MOD

    return (dp1[n - 1] + dp2[n - 1]) % MOD


print(solution(4, [1, 1, 0, 1]))  # 149
print(solution(2, [0, 1]))  # 11
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 7704
