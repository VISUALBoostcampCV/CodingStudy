import heapq as hq

def solution(n, times):
    answer = 0
    
    time_heap = list(zip([0]*len(times), times))
    hq.heapify(time_heap)
    
    while n:
        wait, judge = hq.heappop(time_heap)
        n_wait, n_judge = time_heap[0]
        
        # 처리시간 계산
        judge_time = total_judge_time(wait, judge, answer)
        n_judge_time = total_judge_time(n_wait, n_judge, answer)
        
        # 더 빠른 심사 있으면
        if judge_time > n_judge_time:
            n_wait, n_judge = hq.heappop(time_heap)
            wait, n_wait = n_wait, wait
            judge, n_judge = n_judge, judge
            hq.heappush(time_heap, (n_wait, n_judge))
        
        n -= 1
        hq.heappush(time_heap, (wait+judge, judge))        
        answer = max(answer, wait+judge)    
        
        
    return answer


# 심사 대기시간 + 처리시간 구하기
def total_judge_time(wait, judge, answer):
    total_time = wait + judge
    
    if answer % judge:
        total_time += judge - answer % judge
    
    return total_time



'''
정확성  테스트
테스트 1 〉	실패 (0.03ms, 10.3MB)
테스트 2 〉	실패 (1.53ms, 10.2MB)
테스트 3 〉	실패 (10.23ms, 10.3MB)
테스트 4 〉	실패 (239.12ms, 24.7MB)
테스트 5 〉	실패 (891.40ms, 26MB)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
'''