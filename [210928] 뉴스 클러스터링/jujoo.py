import re
from collections import Counter
from typing import List

# 1 -> O(n)
def solution(str1:str, str2:str) -> int:
    str1, str2 = str1.lower(), str2.lower()

    # O(2n)
    str1_set = [str1[i:i + 2] for i in range(len(str1) - 1) if re.findall('[a-z]{2}', str1[i:i + 2])]
    str2_set = [str2[i:i + 2] for i in range(len(str2) - 1) if re.findall('[a-z]{2}', str2[i:i + 2])]

    try:
        # Counter : O(2n)
        answer = sum((Counter(str1_set) & Counter(str2_set)).values()) / sum((Counter(str1_set) | Counter(str2_set)).values()) # intersection / union
        print(answer)
    except:
        answer = 1

    return int(answer * 65536)


# 2 -> O(n)
def convert(s:str) -> List[str]:
    arr = []
    left, right = 0, 1
    while right < len(s):
        if len(re.findall("[a-z]",s[left] + s[right])) == 2:
            arr.append(s[left] + s[right])
        left += 1
        right += 1
    return arr

def solution(str1:str, str2:str) -> int:
    # O(2n)
    str1 = convert(str1.lower())
    str2 = convert(str2.lower())

    intersec = []
    # O(n)
    check = str2[:]

    # O(n)
    for i in str1:
        if i in check:
            intersec.append(i)
            check.remove(i)
    union = len(str1) + len(str2) - len(intersec)
    if len(intersec) == 0 and union == 0:
        return 65536
    return int(len(intersec) / union * 65536)