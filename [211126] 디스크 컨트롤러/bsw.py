from heapq import heappush, heappop, heapify

def solution(jobs):
    answer = 0
    
    jobs.sort(key = lambda x : -x[0])
    
    len_jobs = len(jobs)
    pq = []
    time = 0
    while jobs or pq:
        if jobs:
            start, work = jobs.pop()
        
            if start < time:
                heappush(pq, [work, start])
                continue
        
        if not pq:
            time += work
            answer += time
        else:
            work, start = heappop(pq)
            answer += time-start + work
            time += work


    return answer // len_jobs
  
  
