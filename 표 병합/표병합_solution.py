parent = [[(r, c) for c in range(51)] for r in range(51)]
cells = [['EMPTY']*51 for _ in range(51)]
result = []

def find(r, c) :
    if (r, c) == parent[r][c] :
        return parent[r][c]
    pr, pc = parent[r][c]
    parent[r][c] = find(pr, pc)
    return parent[r][c]

def union(r1, c1, r2, c2) :
    parent[r2][c2] = parent[r1][c1]

def UPDATE(r, c, msg) :
    pr, pc = find(r, c) 
    cells[pr][pc] = msg

def UPDATE_VAL(msg1, msg2):
    for r in range(51) :
        for c in range(51) :
            pr, pc = find(r, c)
            if cells[pr][pc] == msg1 :
                cells[pr][pc] = msg2
    
def MERGE(r1, c1, r2, c2) :
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    
    if (r1, c1) == (r2, c2) :
        return
    if cells[r1][c1] != "EMPTY" :
        union(r1, c1, r2, c2)
    else :
        union(r2, c2, r1, c1)

def UNMERGE(r, c):
    pr, pc = find(r, c)
    msg = cells[pr][pc]
      
    merge_list = list()
    for ar in range(51) :
        for ac in range(51) :
            apr, apc = find(ar, ac)
            if (apr, apc) == (pr, pc) :
                merge_list.append((ar, ac))
                
    for ar, ac in merge_list :
        parent[ar][ac] = (ar, ac)
        cells[ar][ac] = "EMPTY" if (ar, ac) != (r, c) else msg
    
def PRINT(r, c) :
    pr, pc = find(r, c)
    result.append(cells[pr][pc])
        
def solution(commands):
    for command in commands :
        cmd, *arg = command.split()
        if cmd == "UPDATE" :
            if len(arg) == 3 :
                r, c, value = arg
                UPDATE(int(r), int(c), value)
            else :
                value1, value2 = arg
                UPDATE_VAL(value1, value2)
        elif cmd == "MERGE" :
            r1, c1, r2, c2 = map(int, arg)
            MERGE(r1, c1, r2, c2)
        elif cmd == "UNMERGE" :
            r, c = map(int, arg)
            UNMERGE(r, c)
        else :
            r, c = map(int, arg)
            PRINT(r, c)
            
    return result

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))