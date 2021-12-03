import math
from itertools import permutations
def solution(n, k):
    answer = []
    # [1234][1243][1324][1342][1423][1432]  6
    # [2134][2143][2314][2341][2413][2431]  12
    # [3124][3142][3214][3241][3412][3421]  18  6 2       17  5  1
    # [4123][4132][4213][4231][4312][4321]  24
    f = math.factorial(n)
    lst =  [i+1 for i in range(n)]
    lst_r = [i+1 for i in reversed(range(n))]
    i=0
    # print(lst)
    for v in lst_r:
        f = f//v  # 6 -> 2 -> 1 -> 1
        if k in [0,1]:
            if k==1:
                i = k-1
                k-=1
        else:
            if k%f==0:
                i = (k//f)-1
            else:
                i = k//f  # 02 -> 02 -> 00 -> 00
            k -= i*f  # 18 -> 06 -> 02  
        answer.append(lst[i])
        del lst[i]
    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)

'''