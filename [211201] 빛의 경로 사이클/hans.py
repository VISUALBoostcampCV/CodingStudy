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
    return sorted(answer)

    '''
    테스트 1 〉	통과 (0.65ms, 10.3MB)
    테스트 2 〉	통과 (1.52ms, 10.4MB)
    테스트 3 〉	통과 (1.52ms, 10.3MB)
    테스트 4 〉	통과 (75.30ms, 13.3MB)
    테스트 5 〉	통과 (134.78ms, 16.1MB)
    테스트 6 〉	통과 (167.12ms, 16.9MB)
    테스트 7 〉	통과 (2688.39ms, 99.1MB)
    테스트 8 〉	통과 (1698.37ms, 52.7MB)
    테스트 9 〉	통과 (2228.27ms, 114MB)
    테스트 10 〉	통과 (2599.18ms, 135MB)
    테스트 11 〉	통과 (2948.18ms, 142MB)

    '''