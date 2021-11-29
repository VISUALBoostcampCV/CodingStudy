import heapq
from collections import deque

def solution(jobs):
    n = len(jobs)
    jobs = deque(sorted(jobs)) #criteria start time
    # print(jobs)
    cur_time = work_time = 0 #cur_time is total elapsed time
    cand = []

    while jobs or cand:
        if not cand: #not intersect
            start, time = jobs.popleft()
            cur_time = start + time
            work_time += time

        else: #intersect
            time, start = heapq.heappop(cand)
            cur_time += time
            work_time += cur_time - start

        while jobs and jobs[0][0] <= cur_time:
            heapq.heappush(cand, jobs.popleft()[::-1]) #criteria work time
            
    return work_time // n