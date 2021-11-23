## 맞왜틀...

def change(k, cmd, table, deleted):
    if cmd == "C":
        deleted.append(table.pop(k))
    else:
        d=deleted.pop()
        table.insert(d,d)

def solution(n, k, cmd):
    table = [i for i in range(0, n)]
    deleted=[]
    for c in cmd:
        if c[0] == "D":
            k=k+int(c[2])
        elif c[0] == "U":
            k=k-int(c[2])
        else:
            change(k, c[0], table, deleted) 
            
    answer=["X" for i in range(0,n)]
    for i in table:
        answer[i] ="O"
    return "".join(answer)