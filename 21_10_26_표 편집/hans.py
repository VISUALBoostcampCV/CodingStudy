def down(n,k,d,res):
    for i in range(n):
        while res[d[k+1][0]] == 'X':
            if d[k+1][0] == len(res)-1:
                return k
            d[k+1][0] = d[d[k+1][0]][0]
        k=d[k+1][0]
    return k

def up(n,k,d,res):
    for i in range(n):
        while res[d[k-1][1]] == 'X':
            if d[k-1][1] == 0:
                return k
            d[k-1][1] = d[d[k-1][1]][1]
        k=d[k-1][1]
    return k

def solution(n, k, cmd):
    answer = ''
    d = dict()
    res = ['O']*n
    for i in range(n):
        d[i] = [i-1,i+1]
    d[0][0]=0
    d[n-1][1]=n-1

    deleted = []
    for c in cmd:
        if c[0]=='D':
            for i in range(int(c[-1])):
                k=d[k][1]
        elif c[0]=='U':
            for i in range(int(c[-1])):
                k=d[k][0]
        elif c[0] == 'C':
            res[k] = 'X'
            deleted.append(k)
            u1,d1 = d[k][0], d[k][1]
            d[u1][1]=k
            d[d1][0]=k
            if res[d1]=='X':
                k=u1
            else:
                k=d1
        else:
            p = deleted.pop()
            res[p]='O'
            u1, d1 = p-1, p+1
            d[p] = [u1,d1]
            if u1>=0:
                d[u1][1] = p
                d[d[u1][0]][1]=p
            if d1<n:
                d[d1][0] = p
                d[d[d1][1]][0]=p
            
    return ''.join(res)

# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# s = solution(n,k,cmd2)
# print(s)
