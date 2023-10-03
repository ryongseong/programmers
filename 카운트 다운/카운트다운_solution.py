def solution(target):
    # 가능한 점수는 50점의 경우 "불"의 횟수 1을 추가시키며 리스트를 생성함.
    possible_score = [[50, 1]]

    # 점수판에 1~20까지 있으므로 범위를 설정해줌
    for i in range(1, 21):
        # 1~20까지의 점수를 추가시켜주며 "싱글"의 횟수 1도 같이 추가해줌.
        possible_score.append([i, 1])
        # 2배수의 경우 20점 초과만 함
        if i * 2 > 20:
            # 20점 초과이며 "싱글"이나 "불"이 아니기에 횟수는 0임.
            possible_score.append([i * 2, 0])
        # 3배수의 경우 20점 초과이며 2의 배수가 아니거나 40점 초과일 경우
        if i * 3 > 20 and ((i * 3) % 2 != 0 or i * 3 > 40):
            # 그 점수를 추가시켜주며 "싱글"이나 "불"이 아니기에 횟수는 0임.
            possible_score.append([i * 3, 0])

    # 이건 사실 왜인지 모르겠음. max를 사용하지 않으면 런타임 에러가 발생하게 됨.
    # 인터넷에 검색해서 가져왔음
    dp = [[] for _ in range(max(target + 1, 61))]

    # return값을 만들기 위한 [다트의 개수, "싱글" or "불" 여부]
    for i in range(1, 21):
        # 이 경우 싱글이기에 1번 인덱스에 1
        dp[i] = [1, 1]
        # 아래 두 경우는 "double" and "triple"이기에 1번 인덱스 0
        dp[i * 2] = [1, 0]
        dp[i * 3] = [1, 0]

    # Bull의 경우이기에 50점에 [1, 1]
    dp[50] = [1, 1]

    # 타켓 점수까지만 반환값을 생성하면 되기에 범위를 1점~타겟점수
    for i in range(1, target + 1):
        # 초기화를 위한 배열 생성
        temp_arr = []
        # 다트판에서 한번 던져서 만들어지는 점수가 아닌 경우
        if len(dp[i]) == 0:
            # 위에서 생성한 가능한 점수에서 [가능한 점수, "싱글or불"여부]를 언패킹함
            for p, is_sb in possible_score:
                # i에서 가능한 점수를 뺀 것이 음수일 경우 필요 없기에 넘어가고 양수일때만 따짐
                if i - p > 0:
                    # 초기화를 위한 배열에 던진횟수와 "싱글"+"불"의 경우의 합을 추가시킴
                    temp_arr.append([dp[i - p][0] + 1, dp[i - p][1] + is_sb])

            # 초기화를 위한 배열을 던진횟수는 오름차순으로, "싱글"+"불"의 경우의 합은 내림차순으로 정렬함.
            temp_arr = sorted(temp_arr, key = lambda x : (x[0], -x[1]))
            # 그 점수에 위에서 정렬된 배열을 할당해줌.
            dp[i] = temp_arr[0]
    
    # 이제 우리가 원하는 점수를 반환함.
    return dp[target]

print(solution(58))   