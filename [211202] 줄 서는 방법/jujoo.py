# [블로그 참고]
import math
def solution(n, k):
    # 1~n까지 리스트 정의
    people = [i for i in range(1, n + 1)]
    result = []
    # 끝나는 지점 정의
    end_point = n
    
    while True:
        # n 명일때 줄을 서는 방법은 n!
        f = math.factorial(n - 1)
        # 몫은 해당 인덱스에 있는 값을 가리키고 나머지는 f의 마지막 값인지 아닌지 판단
        q, r = divmod(k, f)
        k = r
        
        if r == 0:
            result.append(people.pop(q - 1))
        else:
            result.append(people.pop(q))
            
        n -= 1 # 사람이 한 명 빠짐
        
        if len(result) == end_point:
            return result