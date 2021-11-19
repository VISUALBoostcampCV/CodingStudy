
import copy

def cal(n1,n2,operate):
    n1=int(n1)
    n2=int(n2)
    if operate=='*':
        return n1*n2
    if operate=='-':
        return n1-n2
    if operate=='+':
        return n1+n2

def ans(e, orders):
    answer_list = []
    stack = []
    exp = copy.copy(e)
    for order in orders:
        for o in order:
            for sub in exp:
                if stack and stack[-1] == o:
                    operate = stack.pop()
                    stack.append(cal(stack.pop(),sub,operate))
                else:
                    stack.append(sub)
            exp = copy.copy(stack)
            stack.clear()
        answer_list.append(abs(exp[0]))
        exp = copy.copy(e)
    return max(answer_list)

def solution(expression):
    answer = 0
    order = [('+','-','*'),('-','+','*'),('-','*','+'),('*','+','-'),
        ('*','-','+'),('+','*','-')]
    for operator in ['+','-','*']:
        expression = expression.replace(operator, f',{operator},')
    expression = expression.split(',')

    return ans(expression, order)




case = "100-200*300-500+20"
case2 ="50*6-3*2"
s = solution(case2)
print(s)

'''
테스트 1 〉	통과 (0.06ms, 10.5MB)
테스트 2 〉	통과 (0.09ms, 10.6MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.09ms, 10.5MB)
테스트 5 〉	통과 (0.16ms, 10.6MB)
테스트 6 〉	통과 (0.16ms, 10.5MB)
테스트 7 〉	통과 (0.10ms, 10.5MB)
테스트 8 〉	통과 (0.10ms, 10.5MB)
테스트 9 〉	통과 (0.10ms, 10.5MB)
테스트 10 〉	통과 (0.21ms, 10.6MB)
테스트 11 〉	통과 (0.23ms, 10.5MB)
테스트 12 〉	통과 (0.12ms, 10.5MB)
테스트 13 〉	통과 (0.13ms, 10.5MB)
테스트 14 〉	통과 (0.15ms, 10.6MB)
테스트 15 〉	통과 (0.15ms, 10.5MB)
테스트 16 〉	통과 (0.08ms, 10.5MB)
테스트 17 〉	통과 (0.06ms, 10.5MB)
테스트 18 〉	통과 (0.10ms, 10.5MB)
테스트 19 〉	통과 (0.05ms, 10.5MB)
테스트 20 〉	통과 (0.06ms, 10.4MB)
테스트 21 〉	통과 (0.29ms, 10.5MB)
테스트 22 〉	통과 (0.14ms, 10.5MB)
테스트 23 〉	통과 (0.05ms, 10.6MB)
테스트 24 〉	통과 (0.19ms, 10.5MB)
테스트 25 〉	통과 (0.18ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.5MB)
테스트 27 〉	통과 (0.28ms, 10.4MB)
테스트 28 〉	통과 (0.17ms, 10.5MB)
테스트 29 〉	통과 (0.16ms, 10.5MB)
테스트 30 〉	통과 (0.16ms, 10.5MB)
'''


# 이전에 풀었던 것
# from collections import deque
# import copy
# def solution(expression):
#     answer = 0
#     d = [('+','-','*'),('-','+','*'),('-','*','+'),('*','+','-'),
#         ('*','-','+'),('+','*','-')]
#     new_exp = deque([])
#     num = ''
#     for ex in expression:
#         if ex in ['-','+','*']:
#             new_exp.append(int(num))
#             new_exp.append(ex)
#             num = ''
#         else:
#             num += ex
#     new_exp.append(int(num))
#     tmp_exp = copy.deepcopy(new_exp)
#     for order in d:
#         for o in order:
#             count = len(tmp_exp)
#             while count > 0:
#                 tmp = tmp_exp.popleft()
#                 count -= 1
#                 if tmp == o:
#                     tmp = tmp_exp.popleft()
#                     count -= 1
#                     if o == '*':
#                         tmp = (tmp_exp.pop() * tmp)
#                     elif o == '+':
#                         tmp = (tmp_exp.pop() + tmp)
#                     elif o == '-':
#                         tmp = (tmp_exp.pop() - tmp)
#                 tmp_exp.append(tmp)
#         answer = max(answer, abs(tmp_exp[0]))
#         tmp_exp = copy.deepcopy(new_exp)
            
#     return answer


'''
테스트 1 〉	통과 (0.10ms, 10.5MB)
테스트 2 〉	통과 (0.16ms, 10.6MB)
테스트 3 〉	통과 (0.14ms, 10.4MB)
테스트 4 〉	통과 (0.16ms, 10.5MB)
테스트 5 〉	통과 (0.19ms, 10.5MB)
테스트 6 〉	통과 (0.15ms, 10.5MB)
테스트 7 〉	통과 (0.18ms, 10.5MB)
테스트 8 〉	통과 (0.20ms, 10.6MB)
테스트 9 〉	통과 (0.24ms, 10.4MB)
테스트 10 〉	통과 (0.24ms, 10.6MB)
테스트 11 〉	통과 (0.21ms, 10.5MB)
테스트 12 〉	통과 (0.24ms, 10.4MB)
테스트 13 〉	통과 (0.28ms, 10.5MB)
테스트 14 〉	통과 (0.32ms, 10.5MB)
테스트 15 〉	통과 (0.32ms, 10.5MB)
테스트 16 〉	통과 (0.16ms, 10.5MB)
테스트 17 〉	통과 (0.11ms, 10.5MB)
테스트 18 〉	통과 (0.13ms, 10.5MB)
테스트 19 〉	통과 (0.11ms, 10.5MB)
테스트 20 〉	통과 (0.12ms, 10.5MB)
테스트 21 〉	통과 (0.34ms, 10.5MB)
테스트 22 〉	통과 (0.32ms, 10.5MB)
테스트 23 〉	통과 (0.09ms, 10.5MB)
테스트 24 〉	통과 (0.31ms, 10.4MB)
테스트 25 〉	통과 (0.30ms, 10.5MB)
테스트 26 〉	통과 (0.11ms, 10.5MB)
테스트 27 〉	통과 (0.33ms, 10.4MB)
테스트 28 〉	통과 (0.32ms, 10.4MB)
테스트 29 〉	통과 (0.30ms, 10.5MB)
테스트 30 〉	통과 (0.30ms, 10.4MB)
'''