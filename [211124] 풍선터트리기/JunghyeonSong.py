def solution(a):    
    # 풍선이 2개 이하면 무조건 남길 수 있음
    if len(a) < 3:
        return len(a)
    
    # 각 방향에서 제일 작은 수
    min_left = a[0]
    min_right = a[-1]
    
    # 풍선 남기는것이 가능한지 체크할 리스트
    check = [False for _a in a]
    check[0] = True
    check[-1] = True
    
    for i in range(1, len(a)-1):
        # 왼쪽 끝부터 체크
        if min_left > a[i]:
            check[i] = True
            min_left = a[i]
        
        # 오른쪽 끝부터 체크
        if min_right > a[-i-1]:
            check[-i-1] = True
            min_right = a[-i-1]
    
    return sum(check)


'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.3MB)
테스트 4 〉	통과 (15.12ms, 14.5MB)
테스트 5 〉	통과 (74.33ms, 36.6MB)
테스트 6 〉	통과 (110.37ms, 48.4MB)
테스트 7 〉	통과 (148.36ms, 63.7MB)
테스트 8 〉	통과 (160.67ms, 63.6MB)
테스트 9 〉	통과 (164.06ms, 63.6MB)
테스트 10 〉	통과 (160.21ms, 63.7MB)
테스트 11 〉	통과 (258.13ms, 63.6MB)
테스트 12 〉	통과 (251.51ms, 63.7MB)
테스트 13 〉	통과 (213.52ms, 63.6MB)
테스트 14 〉	통과 (251.23ms, 63.6MB)
테스트 15 〉	통과 (261.05ms, 63.7MB)
'''