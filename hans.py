import heapq as hq
def solution(jobs):
    answer=0
    div = len(jobs)
    hq.heapify(jobs)
    tmp = []
    cur_s, cur_e = hq.heappop(jobs)
    answer+= cur_e
    while jobs:
        while jobs and jobs[0][0]<=cur_e:
            s,t = hq.heappop(jobs)
            # print(s,e)
            hq.heappush(tmp, (t,s))
        if tmp:
            t, s = hq.heappop(tmp)
        else:
            s, t = hq.heappop(jobs)
            cur_e=s
            
        cur_e+=t
        answer+=cur_e-s
        while tmp:
            t,s = hq.heappop(tmp)
            hq.heappush(jobs, (s,t))
                   
    
    return answer//div

'''
import heapq
def solution(jobs):
    hq = []
    result = []
    end_p = 0
    last = -1
    cnt = 0
    n = len(jobs)
    while cnt < n:
        for job in jobs:
            if end_p >= job[0] > last:
                heapq.heappush(hq, [job[1], job[0]])

        if not hq:
            end_p += 1
        else:
            hqq = heapq.heappop(hq)
            last = end_p
            end_p += hqq[0]
            result.append(hqq[0] + last - hqq[1])
            cnt+=1

    return int(sum(result)/len(result))
'''