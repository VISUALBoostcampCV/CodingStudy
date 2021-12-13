def solution(n, times):
    answer = 0
    left = 1    # 최소 시간
    right = n * max(times)  # 최대 시간
    
    # 이분탐색
    while left < right:
        mid = (left + right) // 2
        total = 0
        
        # 각 심사위원이 주어진 시간동안 심사할 수 있는 인원 더하기
        for time in times:
            total += mid // time               
        
        # 심사할 수 있는 총 인원이 n 이상이면 왼쪽 반 탐색하기
        if total >= n:
            right = mid
        # 심사할 수 있는 총 인원이 n보다 작으면 오른쪽 반 탐색하기
        else:
            left = mid + 1
    
    answer = left   # 최소 시간
    
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (3.71ms, 10.2MB)
테스트 4 〉	통과 (276.01ms, 14.2MB)
테스트 5 〉	통과 (414.98ms, 14.3MB)
테스트 6 〉	통과 (332.12ms, 14.3MB)
테스트 7 〉	통과 (546.60ms, 14.2MB)
테스트 8 〉	통과 (517.43ms, 14.3MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
'''