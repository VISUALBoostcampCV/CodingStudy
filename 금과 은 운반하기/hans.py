import numpy as np
from collections import defaultdict

def solution(a, b, g, s, w, t):
    answer = 0
    d = defaultdict(int)
    ban_list = [1]*len(t)
    t_np = np.array(t)
    last = 0
    while a>0 or b>0:
        t_min = np.min(t_np[ban_list]) if len(t)>1 else t_np[0]
        for i, _t in enumerate(t_np):
            if ban_list[i]==0:
                continue
            new_t = _t-t_min
            if new_t <= 0:
                _g = min(a,g[i],w[i])
                _s = min(b,s[i],w[i]-_g)
                a -= _g
                b -= _s
                new_t = t[i]
                d[i] += 1
            t_np[i] = new_t
            last = i
            if _g==0 and _s==0:
                ban_list[i]=0
    
    print(d)
    
    return max([2*t[k]*v for k,v in d.items()]) - t[last]
a,b,g,s,w,t = 10, 10, [100], [100], [7], [10]
# a,b,g,s,w,t = 90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]
s = solution(a,b,g,s,w,t)
print(s)
'''
테스트 1 〉	통과 (8.01ms, 27.5MB)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	통과 (6643.81ms, 27.9MB)
테스트 4 〉	실패 (9193.64ms, 27.8MB)
테스트 5 〉	실패 (9248.71ms, 28MB)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	실패 (시간 초과)
테스트 22 〉	실패 (시간 초과)
테스트 23 〉	실패 (시간 초과)
테스트 24 〉	통과 (0.36ms, 27.8MB)
'''