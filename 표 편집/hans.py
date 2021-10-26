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
        d[i] = [i,i]
    d[n]=[n-1,n-1]
    d[-1]=[0,0]

    deleted = []
    for c in cmd:
        if c[0]=='D':
            k=down(int(c[-1]),k,d,res)
                
        elif c[0]=='U':
            k=up(int(c[-1]),k,d,res)
        elif c[0] == 'C':
            res[k] = 'X'
            deleted.append(k)
            print(d[k][0])
            d[k][0]=d[k+1][0]
            d[k][1]=d[k-1][1]
            new_k=down(1,k,d,res)
            if new_k==k:
                k=up(1,k,d,res)
        else:
            p = deleted.pop()
            res[p]='O'
            d[p] = (p,p)
            
    return ''.join(res)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
cmd2 = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
s = solution(n,k,cmd2)
print(s)
