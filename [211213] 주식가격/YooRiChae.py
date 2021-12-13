def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1, len(prices)):
            cnt+=1
            if prices[i] <= prices[j]:
                continue
            else:
                break
        answer.append(cnt)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.58ms, 10.3MB)
테스트 4 〉	통과 (0.65ms, 10.3MB)
테스트 5 〉	통과 (0.81ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.36ms, 10.3MB)
테스트 8 〉	통과 (0.68ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.84ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (122.73ms, 18.8MB)
테스트 2 〉	통과 (86.13ms, 17.5MB)
테스트 3 〉	통과 (151.91ms, 19.4MB)
테스트 4 〉	통과 (108.47ms, 18.2MB)
테스트 5 〉	통과 (74.45ms, 17MB)
'''