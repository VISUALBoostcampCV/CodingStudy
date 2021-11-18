# 오쉣 어케풀었지
def twice(rect):
    for idx, (lx,ly,rx,ry) in enumerate(rect):
        rect[idx] = (lx*2,ly*2,rx*2,ry*2)

def solution(rectangle, characterX, characterY, itemX, itemY):
    inside = set()
    land = set()
    move = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = [0]
    footprint = [(characterX*2, characterY*2)]
    twice(rectangle)
    print(rectangle)
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

    for (x, y), c in zip(footprint, cnt):
        for mx, my in move:
            after_x, after_y = x+mx, y+my
            if (after_x, after_y) in footprint:
                continue
            if (after_x, after_y) == (itemX*2, itemY*2):
                return c+1
            elif (after_x, after_y) in land:
                footprint.append((after_x, after_y))
                cnt.append(c+1)


    return land, len(land)



case = ([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1,3,7,8)
case2 = ([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9,7,6,1)
case3 = ([[1,1,5,7]],1,1,4,7)
case4 = ([[2,1,7,5],[6,4,10,10]],3,1,7,10)
s = solution(*case3)
print(s)