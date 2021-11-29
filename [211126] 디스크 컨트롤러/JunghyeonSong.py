import heapq

def solution(jobs):    
    wait_heap = [] 
    answer = jobs[0][1]
    end_time = jobs[0][1] # 현재 작업 종료 예정 시간
    
    for in_time, job_time in jobs[1:]:
        # 작업 중 들어온 요청
        if in_time < end_time:
            total_time = end_time - in_time + job_time
            heapq.heappush(wait_heap, [total_time, job_time])
            continue
        # 작업 끝난 상태에서 들어온 요청
        # 대기중인 작업이 있는 경우
        if wait_heap:
            total_time = end_time - in_time + job_time
            heapq.heappush(wait_heap, [total_time, job_time])
            
            total_time, job_time = heapq.heappop(wait_heap)
            end_time += job_time
            answer += total_time

            for wait in wait_heap:
                wait[0] += job_time
                
        else:
            end_time += job_time
            
    while wait_heap:
        total_time, job_time = heapq.heappop(wait_heap)
        answer += total_time
        
        for wait in wait_heap:
            wait[0] += job_time
            
    
    return answer // len(jobs)


'''
테스트 1 〉	실패 (6.57ms, 10.3MB)
테스트 2 〉	실패 (5.34ms, 10.3MB)
테스트 3 〉	실패 (3.93ms, 10.3MB)
테스트 4 〉	실패 (3.83ms, 10.2MB)
테스트 5 〉	실패 (5.76ms, 10.3MB)
테스트 6 〉	실패 (0.02ms, 10.3MB)
테스트 7 〉	실패 (3.21ms, 10.3MB)
테스트 8 〉	실패 (1.90ms, 10.2MB)
테스트 9 〉	실패 (0.32ms, 10.3MB)
테스트 10 〉	실패 (7.00ms, 10.4MB)
테스트 11 〉	실패 (0.01ms, 10.3MB)
테스트 12 〉	실패 (0.01ms, 10.3MB)
테스트 13 〉	실패 (0.01ms, 10.2MB)
테스트 14 〉	실패 (0.01ms, 10.3MB)
테스트 15 〉	실패 (0.01ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	실패 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	실패 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.00ms, 10.3MB)
'''