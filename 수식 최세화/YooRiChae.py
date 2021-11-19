from itertools import permutations

def calculate(a, o, b):
    if o == "+":
        return int(a) + int(b)
    elif o == "-":
        return int(a) - int(b)
    elif o == "*":
        return int(a) * int(b)
    
def solution(expression):
    def string_to_list(ex):
        stack=[]
        num=""
        for e in expression:
            if e.isdigit():
                stack.append(e)
            else:
                while stack:
                    num+=stack.pop(0)
                ex.append(num)
                num=""
                ex.append(e)
        while stack:
            num+=stack.pop(0)
        ex.append(num)

    def operate(o, ex):
        idx = 0
        while True:
            if ex[idx] == o:
                result = calculate(ex.pop(idx-1), ex.pop(idx-1), ex.pop(idx-1))
                ex.insert(idx-1, result)
                idx-=1
            idx+=1
            if idx >= len(ex) - 1:
                break
            
    ops = ["+", "-", "*"]
    answer = []
    
    ops=list(permutations(ops))
    
    for op in ops:
        ex=[]
        string_to_list(ex)
        
        for o in op:
            operate(o, ex)
        answer.append(abs(ex[0]))
    return max(answer)

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.4MB)
테스트 2 〉	통과 (0.07ms, 10.5MB)
테스트 3 〉	통과 (0.09ms, 10.5MB)
테스트 4 〉	통과 (0.10ms, 10.4MB)
테스트 5 〉	통과 (0.13ms, 10.5MB)
테스트 6 〉	통과 (0.20ms, 10.5MB)
테스트 7 〉	통과 (0.13ms, 10.4MB)
테스트 8 〉	통과 (0.15ms, 10.4MB)
테스트 9 〉	통과 (0.16ms, 10.4MB)
테스트 10 〉	통과 (0.19ms, 10.4MB)
테스트 11 〉	통과 (0.18ms, 10.5MB)
테스트 12 〉	통과 (0.21ms, 10.4MB)
테스트 13 〉	통과 (0.24ms, 10.4MB)
테스트 14 〉	통과 (0.26ms, 10.4MB)
테스트 15 〉	통과 (0.28ms, 10.5MB)
테스트 16 〉	통과 (0.08ms, 10.4MB)
테스트 17 〉	통과 (0.09ms, 10.5MB)
테스트 18 〉	통과 (0.08ms, 10.4MB)
테스트 19 〉	통과 (0.09ms, 10.4MB)
테스트 20 〉	통과 (0.09ms, 10.4MB)
테스트 21 〉	통과 (0.26ms, 10.4MB)
테스트 22 〉	통과 (0.27ms, 10.4MB)
테스트 23 〉	통과 (0.07ms, 10.5MB)
테스트 24 〉	통과 (0.29ms, 10.4MB)
테스트 25 〉	통과 (0.28ms, 10.4MB)
테스트 26 〉	통과 (0.06ms, 10.5MB)
테스트 27 〉	통과 (0.30ms, 10.4MB)
테스트 28 〉	통과 (0.53ms, 10.4MB)
테스트 29 〉	통과 (0.30ms, 10.4MB)
테스트 30 〉	통과 (0.28ms, 10.4MB)
'''