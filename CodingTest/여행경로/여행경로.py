def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))

    def dfs(t, path):
        if len(t) == 0:
            return path

        now = path[-1]
        valid_idx = -1

        for i in range(len(t)):
            if t[i][0] == now:
                valid_idx = i
                break

        if valid_idx == -1:
            return []

        while t[valid_idx][0] == now:
            nxt_path = dfs(t[:valid_idx] + t[valid_idx + 1 :], path + [t[valid_idx][1]])

            if nxt_path != []:
                return nxt_path

            valid_idx += 1
        return []

    return dfs(tickets, ["ICN"])


print(
    solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
)  # ["ICN", "JFK", "HND", "IAD"]

print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)  # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
