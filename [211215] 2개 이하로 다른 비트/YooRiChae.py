def solution(numbers):
    answer = []
    for n in numbers:
        binary = bin(n).replace("0b", "")
        
        if binary.count('1') == len(binary): # 다 1일 경우
            change = len(binary)
        else: # 0이 있을 경우
            change = binary[::-1].index("0") # 가장 밑에 있는 0
            if change == 0: change = 1 # 끝이 0이면 그 앞으로
                
        n=(n+2**change-2**(change-1))
        answer.append(n)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.86ms, 10.5MB)
테스트 2 〉	통과 (109.06ms, 26.1MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.72ms, 10.3MB)
테스트 5 〉	통과 (1.37ms, 10.4MB)
테스트 6 〉	통과 (0.78ms, 10.4MB)
테스트 7 〉	통과 (108.32ms, 25.3MB)
테스트 8 〉	통과 (102.04ms, 24.8MB)
테스트 9 〉	통과 (106.51ms, 24.3MB)
테스트 10 〉	통과 (121.25ms, 26.8MB)
테스트 11 〉	통과 (119.28ms, 26.8MB)
'''