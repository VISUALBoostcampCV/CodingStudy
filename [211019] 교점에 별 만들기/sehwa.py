def meeting_point(a,b):
    
    x = (a[1]*b[2] - a[2]*b[1]) / (a[0]*b[1] - a[1]*b[0])
    y = (a[2]*b[0] - a[0]*b[2]) / (a[0]*b[1] - a[1]*b[0])
    
    if float.is_integer(x) and float.is_integer(y):
        return (x,y)

def solution(line):
    point = []
    for i in range(len(line)-1) :
        for j in range(len(line)-i-1) :
            if line[i][0]*line[j+i+1][1] == line[i][1]*line[j+i+1][0] : # 평행 / 일치하는 직선은 무시
                continue                                         
            point.append(meeting_point(line[i], line[i+1]))
    print(point)
        
    
    return 0