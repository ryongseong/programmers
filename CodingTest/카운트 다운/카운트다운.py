def create():
    lst = []
    lst.append([i for i in range(1, 21)])
    lst[0].append(50)
    nxt = []
    for i in range(1, 21):
        for j in range(2, 4):
            score = i * j
            if score > 20:
                nxt.append(score)

    lst.append(list(set(nxt)))
    return lst

def solution(target):
    table = create()
    inf = float("inf")

    game = [[inf, 0] for _ in range(target+1)]
    game[0][0] = 0
    
    for i in range(1, target+1):
        for j in range(2):
            for k in range(len(table[j])):
                prev = i - table[j][k]

                if prev < 0:
                    continue

                total, valid = game[prev][0] + 1, game[prev][1] + 1 - j

                if total < game[i][0]:
                    game[i] = [total, valid]

                elif total == game[i][0]:
                    game[i] = [total, max(game[i][1], valid)]

    
    return game[target]


print(solution(21))     
# => [1, 0]
# print(solution(58))    
#  # => [2, 2]