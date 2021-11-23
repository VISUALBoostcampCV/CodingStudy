def solution(n, k, cmd):
    answer = ''
    
    lst = ['O' for _ in range(n)]
    undo = []
    
    def left(k, cnt):
        while cnt:
            k -= 1
            cnt -= 1
            if lst[k] == 'X':
                cnt += 1
        return k

    def right(k, cnt):
        while cnt:
            k += 1
            cnt -= 1
            if lst[k] == 'X':
                cnt += 1
        return k
    
    for _, v in enumerate(cmd):
        if len(v) == 1:
            com = v
        else:
            com, cnt = v.split()
        
        if com == 'U':
            k = left(k, int(cnt))
        elif com == 'D':
            k = right(k, int(cnt))
            
        elif com == 'C':
            lst[k] = 'X'
            undo.append(k)
            if k == len(lst)-1:
                k = left(k, 1)
            else:
                k = right(k, 1)
                
        elif com == 'Z':
            z = undo.pop()
            lst[z] = 'O'

    return ''.join(lst)
  
  
  
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.08ms, 10.4MB)
테스트 6 〉	통과 (0.09ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.11ms, 10.5MB)
테스트 9 〉	통과 (0.09ms, 10.5MB)
테스트 10 〉	통과 (0.07ms, 10.4MB)
테스트 11 〉	통과 (0.49ms, 10.5MB)
테스트 12 〉	통과 (0.54ms, 10.5MB)
테스트 13 〉	통과 (0.54ms, 10.4MB)
테스트 14 〉	통과 (1.65ms, 10.4MB)
테스트 15 〉	통과 (2.51ms, 10.5MB)
테스트 16 〉	통과 (1.41ms, 10.5MB)
테스트 17 〉	통과 (6.43ms, 10.5MB)
테스트 18 〉	통과 (5.76ms, 10.5MB)
테스트 19 〉	통과 (5.68ms, 10.4MB)
테스트 20 〉	통과 (5.41ms, 10.4MB)
테스트 21 〉	실패 (런타임 에러)
테스트 22 〉	통과 (2.94ms, 10.5MB)
테스트 23 〉	통과 (0.05ms, 10.5MB)
테스트 24 〉	통과 (0.04ms, 10.4MB)
테스트 25 〉	통과 (0.04ms, 10.5MB)
테스트 26 〉	통과 (0.03ms, 10.5MB)
테스트 27 〉	실패 (런타임 에러)
테스트 28 〉	통과 (0.05ms, 10.5MB)
테스트 29 〉	통과 (0.04ms, 10.4MB)
테스트 30 〉	통과 (0.04ms, 10.4MB)

효율성  테스트
테스트 1 〉	통과 (181.50ms, 22.6MB)
테스트 2 〉	통과 (176.87ms, 22.7MB)
테스트 3 〉	통과 (165.43ms, 22.6MB)
테스트 4 〉	통과 (131.82ms, 29.8MB)
테스트 5 〉	통과 (148.66ms, 29.8MB)
테스트 6 〉 실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉  실패 (시간 초과)
'''
