










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