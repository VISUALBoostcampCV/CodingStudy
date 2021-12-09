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
        
    # 마지막 아파트까지 탐색하지 못한경우
    if left != n+1:
        nowave.append(n-left)
    
    # 전파가 안닿는 부분에 필요한 기지국 최소 갯수 
    area = w*2 +1
    for apart in nowave:
        answer += (apart-1)//area + 1
        
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.4MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.3MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.00ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.00ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (2.29ms, 10.8MB)
테스트 2 〉	통과 (2.54ms, 10.9MB)
테스트 3 〉	통과 (2.57ms, 10.9MB)
테스트 4 〉	통과 (2.60ms, 10.8MB)
'''
