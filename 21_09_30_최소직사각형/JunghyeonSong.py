def solution(sizes):
    # sizes 길이가 1일 경우
    if len(sizes) < 2:
        return sizes[0][0] * sizes[0][1]
    
    # 최대 가로 길이, 최대 세로 길이
    max_w = 0
    max_h = 0   
    
    # O(N)
    for w, h in sizes:
        # 가로길이가 항상 더 길도록 회전
        if w < h:
            w, h = h, w
        
        max_w = w if w > max_w else max_w
        max_h = h if h > max_h else max_h
            
    return max_w * max_h


    '''
    테스트 1 〉	통과 (0.00ms, 10.2MB)
    테스트 2 〉	통과 (0.00ms, 10.2MB)
    테스트 3 〉	통과 (0.00ms, 10.3MB)
    테스트 4 〉	통과 (0.00ms, 10.3MB)
    테스트 5 〉	통과 (0.00ms, 10.2MB)
    테스트 6 〉	통과 (0.00ms, 10.3MB)
    테스트 7 〉	통과 (0.00ms, 10.3MB)
    테스트 8 〉	통과 (0.00ms, 10.2MB)
    테스트 9 〉	통과 (0.01ms, 10.2MB)
    테스트 10 〉	통과 (0.01ms, 10.2MB)
    테스트 11 〉	통과 (0.03ms, 10.2MB)
    테스트 12 〉	통과 (0.03ms, 10.2MB)
    테스트 13 〉	통과 (0.08ms, 10.3MB)
    테스트 14 〉	통과 (0.24ms, 10.5MB)
    테스트 15 〉	통과 (0.23ms, 10.4MB)
    테스트 16 〉	통과 (0.40ms, 10.6MB)
    테스트 17 〉	통과 (0.56ms, 10.9MB)
    테스트 18 〉	통과 (0.65ms, 10.8MB)
    테스트 19 〉	통과 (0.68ms, 11.4MB)
    테스트 20 〉	통과 (0.83ms, 11.4MB)
    '''