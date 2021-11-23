def make_pair(str):
    pair = []
    for p1, p2 in zip(str, str[1:]):
        if p1.isalpha() and p2.isalpha():
            pair.append((p1+p2).lower())
    return pair
def solution(str1, str2):
    answer = 0
    inter = 0
    pair1 = make_pair(str1)
    pair2 = make_pair(str2)
    if len(pair1)+len(pair2)==0:
        return 65536
    
    for p in pair1:
        if p in pair2:
            pair2.remove(p)
            inter += 1
    answer = inter/ (len(pair2) + len(pair1))
    return int(answer*65536)