def solution(a):
    answer = set()
    last = float('inf')
    for left in a:          # 왼쪽부터 탐색
        if left < last:
            last = left
            answer.add(left)    # 제일 작다면 추가
    last = float('inf')
    for right in a[::-1]:   # 오른쪽부터 탐색
        if right < last:
            last = right
            answer.add(right)   # 제일 작다면 추가
        
    return len(answer)

    '''
    테스트 1 〉	통과 (0.01ms, 10.2MB)
    테스트 2 〉	통과 (0.01ms, 10.3MB)
    테스트 3 〉	통과 (0.06ms, 10.2MB)
    테스트 4 〉	통과 (6.40ms, 14.5MB)
    테스트 5 〉	통과 (29.14ms, 33MB)
    테스트 6 〉	통과 (49.72ms, 44.8MB)
    테스트 7 〉	통과 (60.44ms, 56.2MB)
    테스트 8 〉	통과 (64.66ms, 56.2MB)
    테스트 9 〉	통과 (60.39ms, 56.2MB)
    테스트 10 〉	통과 (66.05ms, 56.9MB)
    테스트 11 〉	통과 (275.00ms, 104MB)
    테스트 12 〉	통과 (209.11ms, 104MB)
    테스트 13 〉	통과 (190.39ms, 86.8MB)
    테스트 14 〉	통과 (223.35ms, 104MB)
    테스트 15 〉	통과 (220.07ms, 104MB)
    '''