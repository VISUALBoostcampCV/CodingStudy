'''1차시도'''
# def solution(a):
#     answer = 2
    
#     # 3개 남았을때 가운데 수가 가장 큰 수가 되면 안된다
#     # 양쪽 끝에 있는 수는 반드시 최후까지 남을 수 있음
    
#     # minleft, minright = 1000000000 + 1, 1000000000 + 1
#     for i in range(1, len(a)-1):
#         # slicing * min = O(N^2) ... 시간초과
#         # O(N) 으로 해결해야 한다

#         minleft = min(a[:i])
#         minright = min(a[i+1:])
        
#         if a[i] != max(minleft, a[i], minright):
#             answer += 1
        
#     return answer

'''2차 시도'''
# def solution(a):
#     answer = 2
    
#     minleft = deque([a[0]])
#     minright = deque([a[-1]])
    
#     for i in range(1, len(a)):
#         minleft.append(min(minleft[i-1], a[i]))
        
#     for i in range((len(a)-1) -1, -1, -1):
#         minright.appendleft(min(minright[i+1], a[i]))

        
#     for i in range(1, len(a)-1):
#         if a[i] != max(a[i], minleft[i-1], minright[i+1]):
#             answer += 1

#     return answer


'''
3차 시도

2차랑 3차랑 대체 무슨 차이길래 2차는 시간초과나고 3차는 안나는 걸까요?
'''
from collections import deque

def solution(a):
    answer = 2
    
    minleft = [0]*len(a)
    minright = [0]*len(a)
    
    minleft[0] = a[0]
    minright[-1] = a[-1]
    
    for i in range(1, len(a)):
        minleft[i] = min(minleft[i-1], a[i])
        
    for i in range((len(a)-1) -1, -1, -1): # i 는 -2번째 idx부터 0번 idx까지 오른쪽에서 왼쪽으로 이동
        minright[i] = min(minright[i+1], a[i])

        
    for i in range(1, len(a)-1):
        if a[i] != max(a[i], minleft[i-1], minright[i+1]):
            answer += 1

    return answer



