import string
from collections import Counter

def solution(str1, str2):
    alpha = string.ascii_letters
    
    list1 = [(i+j).lower() for i, j in zip(str1, str1[1:]) if i in alpha and j in alpha]
    list2 = [(i+j).lower() for i, j in zip(str2, str2[1:]) if i in alpha and j in alpha]
    
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    n = 0
    
    for key in counter1:
        n += min(counter1[key], counter2[key])
        
    u = len(list1) + len(list2) - n
    
    if u == 0:
        return 65536    
    
    return int(n / u * 65536)