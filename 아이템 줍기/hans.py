# 어렵네요...

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    inside = set()
    land = set()
    for lx,ly,rx,ry in rectangle:
        for x in range(lx+1,rx):
            for y in range(ly+1,ry):
                inside.add((x, y))
                
    for lx,ly,rx,ry in rectangle:
        for x in range(lx, rx+1):
            if (x, ly) not in inside:
                land.add((x,ly))
            if (x, ry) not in inside:
                land.add((x,ry))
        for y in range(ly, ry+1):
            if (lx, y) not in inside:
                land.add((lx,y))
            if (rx, y) not in inside:
                land.add((rx,y))


    return land, len(land)



case = ([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1,3,7,8)
case2 = ([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9,7,6,1)
s = solution(*case2)
print(s)