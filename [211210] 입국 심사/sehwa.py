def solution(n, times):
    answer = 0
    
    times.sort()
    
    first = 1
    last = times[len(times)-1]*n
    mid = 0
    
    while first < last :
        mid = (first + last) // 2
        sum = 0
        for time in times:
            sum += mid // time
        if sum >= n :
            last = mid
        elif sum < n :
            first = mid + 1
            
    answer = first
    print(mid)
    
    return answer



'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.16ms, 10.2MB)
테스트 3 〉	통과 (4.32ms, 10.3MB)
테스트 4 〉	통과 (345.45ms, 14.1MB)
테스트 5 〉	통과 (484.99ms, 14.3MB)
테스트 6 〉	통과 (336.15ms, 14.3MB)
테스트 7 〉	통과 (612.73ms, 14.2MB)
테스트 8 〉	통과 (642.72ms, 14.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
'''