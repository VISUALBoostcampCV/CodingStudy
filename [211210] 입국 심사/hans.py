import bisect
import math

def solution(n, times):
    start = min(times) * math.ceil(n/len(times))
    end = max(times) * n
    
    while (end-start) != 1:
        middle = (start+end) // 2
        tmp = 0
        for time in times:
            tmp += middle//time
        if tmp >= n:
            end = middle
        elif tmp < n:
            start = middle
    
    return end

테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.10ms, 10.3MB)
테스트 3 〉	통과 (3.71ms, 10.3MB)
테스트 4 〉	통과 (282.17ms, 14.3MB)
테스트 5 〉	통과 (427.95ms, 14.2MB)
테스트 6 〉	통과 (301.45ms, 14.3MB)
테스트 7 〉	통과 (545.30ms, 14.2MB)
테스트 8 〉	통과 (523.35ms, 14.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)




''' Old Code

import math
def solution(n, times):
    times.sort()
    left = math.ceil(n/len(times))*times[0]
    right = math.ceil(n/len(times))*times[-1]
    if times[0] == times[-1]:
        return left
    while 1:
        middle = int((left+right)/2)
        if left == middle:
            return right
        #print(left, middle, right)
        tmp = 0
        flag = False
        for time in times:
            if middle % time == 0:
                flag = True
            tmp += int(middle/time)
        if tmp < n:
            left = middle
        elif tmp > n:
            right = middle
        elif flag:
            return middle
        else:
            right = middle+1



테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.35ms, 10.2MB)
테스트 3 〉	통과 (6.67ms, 10.1MB)
테스트 4 〉	통과 (511.18ms, 14.3MB)
테스트 5 〉	통과 (632.61ms, 14.3MB)
테스트 6 〉	통과 (469.89ms, 14.3MB)
테스트 7 〉	통과 (959.72ms, 14.4MB)
테스트 8 〉	통과 (939.14ms, 14.2MB)
테스트 9 〉	통과 (0.10ms, 10.3MB)

'''