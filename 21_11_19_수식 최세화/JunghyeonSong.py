from itertools import permutations

def solution(expression):
    answer = 0

    # 연산자 우선순위 순열 리스트 생성
    priority_list = list(map(list, permutations(['+', '-', '*'], 3)))
    
    # 각 순열 별로 수식을 계산해보고 절대값이 최대인 경우를 저장
    for priority in priority_list:
        answer = max(answer, abs(calculator(expression, priority, 2)))   
    
    return answer


'''
calculator(expression, priority_list, p_index)
expression: 수식
priority_list: 연산자 우선순위 순열. 제일 마지막 인덱스에 있는 연산자가 제일 낮은 우선순위를 가진다고 설정함
                 ex. ['+', '-', '*'] => * 연산자가 제일 낮은 우선순위
'''
def calculator(expression, priority_list, p_index):
    # 아직 split 할 수 있다면 (연산자가 남아있다면)
    if p_index > -1:
        # 지정된 연산자로 split
        oper = priority_list[p_index]
        splited_exp = expression.split(oper)
        
        # 다음 우선순위 연산자로 설정
        p_index -= 1

        # split한 첫번째 인자를 result에 넣어서 다음 인자와 연산할 수 있게 함
        result = calculator(splited_exp[0], priority_list, p_index)
        
        # 두번째 인자부터 for문 돌면서 연산 진행
        for i in range(1, len(splited_exp)):
            # 이전 계산 결과와 다음 계산 결과를 합침
            # 어차피 같은 우선순위 연산만 진행되므로 괜찮음
            result = calculate(result, calculator(splited_exp[i], priority_list, p_index), oper)
        
        return result        

    # split 할 수 없다면 (연산자 기준 split 모두 진행한 상태)
    # 숫자만 남아있게 됨. string을 int로 형변환하여 반환
    else:
        return int(expression)
        

# 주어진 수와 연산자에 맞게 계산 후 리턴    
def calculate(a, b, oper):
    a = int(a)
    b = int(b)
    if oper == '+':
        return a+b
    elif oper == '-':
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