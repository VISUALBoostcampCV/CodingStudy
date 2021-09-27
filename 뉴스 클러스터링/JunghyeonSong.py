import string
from collections import Counter

def solution(str1, str2):
    alpha = string.ascii_letters
    
    list1 = [(i+j).lower() for i, j in zip(str1, str1[1:]) if i in alpha and j in alpha]    # O(N)
    list2 = [(i+j).lower() for i, j in zip(str2, str2[1:]) if i in alpha and j in alpha]    # O(N)
    
    counter1 = Counter(list1)   # O(N)
    counter2 = Counter(list2)   # O(N)
    
    n = 0
    
    # O(N)
    for key in counter1:
        n += min(counter1[key], counter2[key])

    u = len(list1) + len(list2) - n # O(1)
    
    if u == 0:
        return 65536    
    
    return int(n / u * 65536)


'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.56ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.09ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (0.13ms, 10.2MB)
테스트 11 〉	통과 (0.15ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.3MB)
'''