import re

def divide_expression(expression):
    '''
    숫자와 연산자를 나누어 numbers, operators로 리턴
    '''
    
    numbers = list(map(int,re.split('[-,+,*]',expression)))        # 연산자를 기준으로 숫자를 추출
    operators = re.findall('[-,+,*]',expression)    # 연산자 추출
        
    return numbers, operators


def calculate(numbers, operators, prior):
    '''
    주어진 숫자를 연산자 우선순위로 계산
    '''
    for p in prior:
        for i, o in enumerate(operators): 
            if p is not o:
                continue
            if o == '*':
                numbers[i] = numbers[i] * numbers.pop(i+1)
                operators.pop(i)
            elif o == '+':
                numbers[i] = numbers[i] + numbers.pop(i+1)
                operators.pop(i)
            elif o == '-':
                numbers[i] = numbers[i] - numbers.pop(i+1)
                operators.pop(i)

    return numbers[0]


def solution(expression):
    answer = 0
    priorities = [['*','+','-'], ['*','-','+'], ['+','*','-'], ['+','-','*'], ['-','*','+'],['-','+','*']]
    numbers, operators = divide_expression(expression)
    
    for prior in priorities:
        numbers = calculate(numbers, operators, prior)
        
        if answer < abs(numbers):
            answer = abs(numbers)
    
    return answer


'''
여려분 오늘 참여하지 못해서 너무 죄송합니당...
코드는 뭐가 틀린걸까요...
'''