from math import factorial


def solution(n, k):
    answer = []
    line = list(range(1,n+1)) # [1,2,3,4,...,n]
    k = k-1 # 순서 하나 +1 되는 것 ㅈㅔ거, index 수 맞추기
    
    for i in range(n,0,-1): # n! - 1 까지 돌기
        print(i)
        div, k = divmod(k, factorial(i-1))
        print(div, k)
        answer.append(line.pop(div))
        print(answer)
    
    return answer
    
    
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.06ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.10ms, 10.1MB)


'''

