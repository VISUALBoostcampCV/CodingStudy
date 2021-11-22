from itertools import product
from collections import deque

def chk_zero(Map, y,x):
    flag=0
    for ny, nx in (-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1):
        if 0<=y+ny<50 and 0<=x+nx<50 and Map[y+ny][x+nx] == 0 :
            flag = 1
    if flag:
        return True
    return False


def del_inside(Map):
    lst=[]
    for i in range(50):
        for j in range(50):
            if not chk_zero(Map, i,j):
                lst.append((i,j))
    
    for y, x in lst:
        Map[y][x] = 0
        

def bfs(Map, a, b, A, B):
    q = deque([(b,a)])
    visited = [(b,a)]
    
    result = 0
    while q:
        y, x = q.popleft()
        if (y,x) == (B,A):
            break
        for ry, rx in (-1,0), (1,0), (0,1), (0,-1):
            ny, nx = y+ry, x+rx
            
            if (ny, nx) in visited:
                continue
            if Map[ny][nx]:
                q.append((ny,nx))
                visited.append((ny,nx))
                
    
    return result
                

        

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    Map = [[0] * 50 for _ in range(50)]
    
    for xy in rectangle:
        x1, y1, x2, y2 = xy
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2

        Xs = [x1 + x for x in range(x2-x1+1)]#1 2 3 4 5 6 7
        Ys = [y1 + y for y in range(y2-y1+1)]#1 2 3 4
        # print(Xs)
        p = list(product(Xs, Ys))
        # print(p)
        for x,y in p:
            Map[y][x] += 1
            
    del_inside(Map)
    
    for i in range(20,0,-1):
        print(Map[i][:20])
        
    answer = bfs(Map, characterX, characterY, itemX, itemY)
    print(answer)
    
    
    return answer
