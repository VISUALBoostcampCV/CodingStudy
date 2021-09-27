def getarray(s):
    arr=[]
    for i in range(len(s)-1): 
        if s[i:i+2].isalpha():          
            arr.append(s[i:i+2].lower())
    return arr

def solution(str1, str2):    
    A = getarray(str1)
    B = getarray(str2)
    if A == B: return 65536
    
    interset = A + B
    sumset = []
    
    for pair in A:
        if pair in B:
            sumset.append(pair)
            interset.remove(pair)
            B.remove(pair)
    
    return int(len(sumset) / len(interset) * 65536)


'''
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.77ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.13ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.2MB)
테스트 10 〉	통과 (0.30ms, 10.3MB)
테스트 11 〉	통과 (0.22ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
'''