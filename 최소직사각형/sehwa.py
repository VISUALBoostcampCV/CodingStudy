def solution(sizes):
    
    maxwidth = 0
    maxheight = 0
    
    
    for w, h in sizes:
        if w < h : # w가 항상 더 길게 유지
            temp = w
            w = h
            h = temp
        if maxwidth < w :
            maxwidth = w
        if maxheight < h :
            maxheight = h
    
    answer = maxwidth * maxheight
    return answer




# 테스트 1 〉	통과 (0.00ms, 10.1MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.2MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.02ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.2MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.16ms, 10.5MB)
# 테스트 15 〉	통과 (0.23ms, 10.5MB)
# 테스트 16 〉	통과 (0.35ms, 10.6MB)
# 테스트 17 〉	통과 (0.71ms, 10.9MB)
# 테스트 18 〉	통과 (0.87ms, 10.9MB)
# 테스트 19 〉	통과 (0.55ms, 11.4MB)
# 테스트 20 〉	통과 (0.70ms, 11.3MB)