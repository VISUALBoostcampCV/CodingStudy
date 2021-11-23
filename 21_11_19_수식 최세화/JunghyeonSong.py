from itertools import permutations

def solution(expression):
    answer = 0    
    priority_list = list(map(list, permutations(['+', '-', '*'], 3)))
    
    for priority in priority_list:
        answer = max(answer, abs(calculator(expression, priority, 2)))   
    
    return answer

def calculator(expression, priority_list, p_index):    
    if p_index > -1:
        cal = priority_list[p_index]
        splited_exp = expression.split(cal)
        p_index -= 1
        
        result = calculator(splited_exp[0], priority_list, p_index)
        
        for i in range(1, len(splited_exp)):
            result = calculate(result, calculator(splited_exp[i], priority_list, p_index), cal)
        
        return result        
        
    else:
        return int(expression)
        
    
def calculate(a, b, cal):
    a = int(a)
    b = int(b)
    if cal == '+':
        return a+b
    elif cal == '-':
        return a-b
    else:
        return a*b


'''
테스트 1 〉	통과 (0.06ms, 10.4MB)
테스트 2 〉	통과 (0.06ms, 10.5MB)
테스트 3 〉	통과 (0.07ms, 10.4MB)
테스트 4 〉	통과 (0.08ms, 10.5MB)
테스트 5 〉	통과 (0.17ms, 10.5MB)
테스트 6 〉	통과 (0.10ms, 10.5MB)
테스트 7 〉	통과 (0.10ms, 10.4MB)
테스트 8 〉	통과 (0.12ms, 10.4MB)
테스트 9 〉	통과 (0.20ms, 10.5MB)
테스트 10 〉	통과 (0.14ms, 10.4MB)
테스트 11 〉	통과 (0.12ms, 10.4MB)
테스트 12 〉	통과 (0.15ms, 10.4MB)
테스트 13 〉	통과 (0.15ms, 10.4MB)
테스트 14 〉	통과 (0.17ms, 10.4MB)
테스트 15 〉	통과 (0.17ms, 10.5MB)
테스트 16 〉	통과 (0.06ms, 10.4MB)
테스트 17 〉	통과 (0.06ms, 10.4MB)
테스트 18 〉	통과 (0.06ms, 10.4MB)
테스트 19 〉	통과 (0.09ms, 10.4MB)
테스트 20 〉	통과 (0.07ms, 10.5MB)
테스트 21 〉	통과 (0.27ms, 10.4MB)
테스트 22 〉	통과 (0.16ms, 10.4MB)
테스트 23 〉	통과 (0.05ms, 10.4MB)
테스트 24 〉	통과 (0.18ms, 10.4MB)
테스트 25 〉	통과 (0.29ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.4MB)
테스트 27 〉	통과 (0.18ms, 10.5MB)
테스트 28 〉	통과 (0.18ms, 10.4MB)
테스트 29 〉	통과 (0.15ms, 10.4MB)
테스트 30 〉	통과 (0.18ms, 10.4MB)
'''