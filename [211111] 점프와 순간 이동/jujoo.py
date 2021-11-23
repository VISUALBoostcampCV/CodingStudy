def sq(n : int):
    if n == 1:
        return True
    q, r = divmod(n, 2)
    if r == 0:
        sq(q)
    else:
        return

def solve(n:int, alpha : int):
    if n < 10 and n % 2 == 1:
        return n, alpha
    elif n >= 10 and n % 2 == 1:
        alpha += 1
        return solve(n - 1, alpha)
    n = n // 2
    return solve(n, alpha)
    
def solution(n : int):
    dic = {1 : 1, 3 : 2, 5 : 2, 7 : 3, 9 : 2}
    
    if n <= 2 or sq(n):
        return 1
    
    if n in dic:
        return dic[n]
    
    if n % 2 == 0:
        n, alpha = solve(n, 0)
        answer = dic[n] + alpha
    else:
        n, alpha = solve(n - 1, 0)
        answer = dic[n] + alpha + 1
    return answer

# 테스트 1 〉	통과 (0.00ms, 10.3MB)
# 테스트 2 〉	통과 (0.00ms, 10.3MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.3MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.3MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.3MB)