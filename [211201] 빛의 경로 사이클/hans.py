from collections import defaultdict

def rotate(v, s):
    if s=='R':
        if v[0]==0:
            return [v[1],v[0]]
        else:
            return [v[1],-v[0]]
    elif s=='L':
        if v[0]==0:
            return [-v[1],v[0]]
        else:
            return [v[1],v[0]]
    return v

def cut(p, length):
    if p==-1:
        p=length-1
    elif p==length:
        p=0
    return p

def search(g, p, v, mem):
    cnt = 0
    while v not in mem[str(p)]:
        mem[str(p)].append(v)
        cnt+=1
        p[0] = cut(p[0]+v[0],len(g))
        p[1] = cut(p[1]+v[1],len(g[0]))
        new_v = g[p[0]][p[1]]
        v = rotate(v, new_v)
    return cnt

def solution(grid):
    answer = []
    mem = defaultdict(list)
    move = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for my,mx in move:
                cnt = search(grid,[y,x],[my,mx],mem)
                if cnt:
                    answer.append(cnt)        
    return answer