def create():
    dart_table = []
    dart_table.append([i for i in range(1, 21)])
    dart_table[0].append(50)
    
    double_triple_dart = []
    for j in range(1, 21):
        for k in range(2, 4):
            score = j * k

            if score > 20:
                double_triple_dart.append(score)

    dart_table.append(list(set(double_triple_dart)))

    return dart_table

def solution(target):
    dart_table = create()
    inf = float("inf")

    dart_game = [[inf, 0] for _ in range(target+1)]
    dart_game[0][0] = 0

    for i in range(1, target+1):
        for j in range(2):
            for k in range(len(dart_table[j])):
                prev_score = i - dart_table[j][k]

                if prev_score < 0:
                    continue

                total, valid = dart_game[prev_score][0] + 1, dart_game[prev_score][1] + 1 - j

                if total < dart_game[i][0]:
                    dart_game[i] = [total, valid]
                
                elif total == dart_game[i][0]:
                    dart_game[i] = [total, max(dart_game[i][1], valid)]

    return dart_game[target]

print(solution(58))    
#  # => [2, 2]