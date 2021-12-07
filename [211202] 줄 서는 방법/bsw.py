
def factorial(n):
    result = 1
    
    if n == 1:
        return n
    for i in range(2, n+1):
        result *= i
        
    return result

def solution(n, k):
    answer = []
    
    nums = [i for i in range(1, 20 +1)]
    
    while n:
        slice = factorial(n) // n
        now = (k-1) // slice
        answer.append(nums.pop(now))

        n-=1
        k %= slice
        if k == 0:
            k = slice

    return answer
