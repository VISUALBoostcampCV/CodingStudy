def solution(sizes):
    answer = 0
    
    Widths=[]
    Heights=[]
    for size in sizes:
        x, y = size
        
        if x>=y :
            Widths.append(x)
            Heights.append(y)
        else:
            Widths.append(y)
            Heights.append(x)
    
    return max(Widths)*max(Heights)
