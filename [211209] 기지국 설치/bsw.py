# O(n)으로 끝내야함
def solution(n, stations, w):
    answer = 0
    
    nowave = []
    
    # 전파가 안닿는 범위들을 탐색
    left = 0
    for station in stations:
        right = station - w -1
        nowave.append(right-left)
        left = station + w
        
    if left != n+1:
        nowave.append(n-left)
    
    # 전파가 안닿는 부분에 필요한 기지국 최소 갯수 
    area = w*2 +1
    for apart in nowave:
        answer += (apart-1)//area + 1
        
    return answer
