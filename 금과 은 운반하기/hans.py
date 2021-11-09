import numpy as np
import heapq as hq
from collections import defaultdict


def solution(a, b, g, s, w, t):
    answer = 0
    last = -1
    d = defaultdict(int)
    new_t = [(v, i) for i,v in enumerate(t)]
    hq.heapify(new_t)
    # print(new_t)
    
    while a>0 or b>0:
        p = hq.heappop(new_t)
        i=p[1]
        _g = min(a,g[i],w[i])
        _s = min(b,s[i],w[i]-_g)
        a -= _g
        b -= _s
        d[i] += 1
        last = i
        
        if _g>0 or _s>0:
            hq.heappush(new_t, (p[0]+t[i],p[1]))
            
    print(d)
    return max([2*t[k]*v for k,v in d.items()]) - t[last]
a,b,g,s,w,t = 10, 10, [100], [100], [7], [10]
# a,b,g,s,w,t = 90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1]
s = solution(a,b,g,s,w,t)
print(s)