def solution(n, times):
    answer = 0
    
    def check(time):    # 몇명이 입국심사 할 수 있는지
        people=0
        for examiner in times:
            people+=time//examiner
        return people
    
    start = 0
    end = 1e18  # 최대 걸리는 시간 1,000,000,000분 * 1,000,000,000명

    while start <= end:
        mid = (start + end) // 2

        if check(mid) < n:
            start = mid + 1
        else:
            end = mid -1
            
    return start
    
'''
정확성  테스트
테스트 1 〉	통과 (0.12ms, 10.2MB)
테스트 2 〉	통과 (1.01ms, 10.2MB)
테스트 3 〉	통과 (8.56ms, 10.3MB)
테스트 4 〉	통과 (809.04ms, 14.3MB)
테스트 5 〉	통과 (828.82ms, 14.2MB)
테스트 6 〉	통과 (1120.28ms, 14.2MB)
테스트 7 〉	통과 (981.15ms, 14.3MB)
테스트 8 〉	통과 (1005.21ms, 14.2MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
'''