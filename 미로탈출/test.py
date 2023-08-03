import heapq
traps = [2, 3]

mask_idx = {t : n for n, t in enumerate(traps)}

heap = [(0,1,0)]
d,idx, mask = heapq.heappop(heap)
print(mask_idx)

print(1 << mask_idx[2])