def create():
    # 다트 판에서 만들 수 있는 점수를 위한 리스트
    dart_table = []
    # 1~20점은 그냥 있으니 추가
    dart_table.append([i for i in range(1, 21)])
    # 리스트 제일 앞에 "불"일 경우의 50점 추가
    dart_table[0].append(50)
    
    # 2배수나 3배수를 위한 다트판 점수 리스트
    double_triple_dart = []
    # 1~20까지 있으니 범위를 지정해줌.
    for j in range(1, 21):
        # 2배수, 3배수가 있으니 2~3까지 범위 지정
        for k in range(2, 4):
            # 점수는 j*k임.
            score = j * k
            
            # 점수가 20점 초과가 아닐 경우 싱글일 때가 더 유리하므로 20점 초과만 리스트에 담음
            if score > 20:
                double_triple_dart.append(score)

    # 2배수나 3배수의 경우 겹치는 부분도 있기에 set형으로 중복을 다 날리고, 다시 list형태로 변경 후 다트 점수 리스트에 추가시킴.
    dart_table.append(list(set(double_triple_dart)))

    # 만들어진 다트판을 반환함.
    return dart_table

def solution(target):
    # 위에서 만든 다트판을 위한 함수를 불러 dart_table에 만들어진 다트판을 할당해줌.
    dart_table = create()
    # inf에 무한대를 할당해줌.
    inf = float("inf")

    # 다트 게임에서 만들 수 있는 모든 경우가 있기에 target까지 모두 [무한대, 0] 형태의 이차원 배열로 게임을 생성
    dart_game = [[inf, 0] for _ in range(target+1)]
    # 0번 인덱스의 경우 다트를 던지는 것이 아니기에 0으로 덮어씌워줌
    dart_game[0][0] = 0

    # 1점부터 원하는 점수까지를 돌림
    for i in range(1, target+1):
        # 이차원 리스트이며, 리스트 안에 리스트가 1번 인덱스까지 있으므로 범위를 2로 지정
        for j in range(2):
            # 만들 수 있는 모든 점수를 가정함.
            for k in range(len(dart_table[j])):
                # ㄷ
                prev_score = i - dart_table[j][k]

                if prev_score < 0:
                    continue

                total = dart_game[prev_score][0] + 1 
                valid = dart_game[prev_score][1] + 1 - j

                if total < dart_game[i][0]:
                    dart_game[i] = [total, valid]
                
                elif total == dart_game[i][0]:
                    dart_game[i] = [total, max(dart_game[i][1], valid)]

    return dart_game[target]

print(solution(58))    
#  # => [2, 2]