def checknum(a, b):
    a ,b = bin(a)[2:], bin(b)[2:]
    
    sub = len(a)-len(b)
    if sub != 0:
        if sub<0:
            a = '0'*abs(sub) + a
        elif sub>0:
            b = '0'*sub + b
    
    num=0
    for i in range(1, len(a)+1):
        if a[-i] != b[-i]:
            num+=1
        if num == 3:
            return False
        
    return True
        

def solution(numbers):
    answer = []
    
    for number in numbers:
        num2 = number
        while 1:
            num2 += 1
            # 비트차이 2개
            if checknum(number, num2):
                answer.append(num2)
                break
            
    return answer
  
  '''
  정확성  테스트
테스트 1 〉	통과 (3.97ms, 10.3MB)
테스트 2 〉	통과 (718.65ms, 23MB)
테스트 3 〉	통과 (0.78ms, 10.4MB)
테스트 4 〉	통과 (3.64ms, 10.3MB)
테스트 5 〉	통과 (9.83ms, 10.3MB)
테스트 6 〉	통과 (6.55ms, 10.5MB)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	실행 중단
테스트 11 〉	실행 중단
'''
