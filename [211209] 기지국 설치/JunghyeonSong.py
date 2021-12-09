def solution(n, stations, w):
    answer = 0
    prv_w = 1 # 현재까지 커버되는 인덱스
    w_area = 2 * w + 1    # 기지국 커버 범위
    
    for station in stations:
        q, r = divmod(station - w - prv_w, w_area)        
        answer +=  q + (1 if r > 0 else 0)
        prv_w = station + w + 1  
    
    if prv_w < n:
        q, r = divmod(n - prv_w, w_area)
        answer +=  q + (1 if r > 0 else 0)

    return answer


'''
정확성  테스트
테스트 1 〉	실패 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.4MB)
테스트 3 〉	통과 (0.00ms, 10.4MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	실패 (0.00ms, 10.3MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.4MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (2.55ms, 10.5MB)
테스트 2 〉	통과 (2.53ms, 10.5MB)
테스트 3 〉	통과 (2.70ms, 10.5MB)
테스트 4 〉	통과 (2.70ms, 10.6MB)
'''