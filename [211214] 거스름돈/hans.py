'''
  1  2  3  4  5  6  7  8  9  10
1 1  1  1  1  1  1  1  1  1  1
2 0  1  0  1  0  1  0  1  0  1
3 0  0  1  0  0  1  0  0  1  0
4 0  0  0  1  0  0  0  1  0  0
5 0  0  0  0  1  0  0  0  0  1
'''


def solution(n, money):
    answer = 0
    money_map = []
    for i in range(n):
        tmp = []
        for m in money:
            if (i+1)%m==0:
                tmp.append(1)
            else:
                tmp.append(0)
        money_map.append(tmp)
    
    key = money_map[-1]
    for m in money_map[:-1]:
        for i, _m in enumerate(m):
            if key[i]:
                answer += m[i+1:].count(1)
    answer += key.count(1)
    
    return answer