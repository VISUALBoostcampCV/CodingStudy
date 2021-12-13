def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)] # 초기 값 [4,3,2,1,0]
    stack = []

    for i, price in enumerate(prices):
        while stack and price < stack[-1][0]:        # 가격이 떨어진다면
            p, j = stack.pop()
            answer[j] = i-j                          # 갱신
        stack.append((price, i))

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.22ms, 10.3MB)
테스트 4 〉	통과 (0.27ms, 10.3MB)
테스트 5 〉	통과 (0.31ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.16ms, 10.3MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.32ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (29.17ms, 19.4MB)
테스트 2 〉	통과 (22.69ms, 17.9MB)
테스트 3 〉	통과 (32.62ms, 20.3MB)
테스트 4 〉	통과 (22.33ms, 18.6MB)
테스트 5 〉	통과 (17.91ms, 17.3MB)

'''


''' 이전 코드
def solution(prices):
    count = 0
    answer = []
    len_p = len(prices)
    for i in range(len_p-1):
        for j in range(i+1,len_p):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)
        count = 0
    answer.append(0)
    return answer


테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.59ms, 10.3MB)
테스트 4 〉	통과 (0.62ms, 10.3MB)
테스트 5 〉	통과 (2.39ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.35ms, 10.4MB)
테스트 8 〉	통과 (0.71ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (1.26ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (119.35ms, 18.8MB)
테스트 2 〉	통과 (92.41ms, 17.5MB)
테스트 3 〉	통과 (147.28ms, 19.6MB)
테스트 4 〉	통과 (105.34ms, 18.3MB)
테스트 5 〉	통과 (72.37ms, 17.1MB)
'''