import math
def solution(N, stations, W):
    def good(station):
        for i in range(-W,W+1):
            if station+i < N and station+i > -1:
                houses[station+i] = 1
    answer = 0

    houses = [0 for i in range(N)]
    for station in stations:
        good(station-1)
    empty = 0
    for idx in range(N):
        if houses[idx] or idx == N-1:
            if idx==N-1 and not houses[idx]: empty+=1
            answer+=math.ceil(empty/(2*W+1))
            empty=0
        else:
            empty+=1
        
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.04ms, 10.3MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.04ms, 10.3MB)
테스트 20 〉	통과 (0.03ms, 10.3MB)
테스트 21 〉	통과 (0.06ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
'''