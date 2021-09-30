def solution(sizes):
    W=[]
    H=[]
    for i,(w,h) in enumerate(sizes):
        if w > h:
            W.append(h) 
            H.append(w)
        else:
            W.append(w) 
            H.append(h)
    
    answer = max(H) * max(W)
    return answer

'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.09ms, 10.3MB)
테스트 13 〉	통과 (0.16ms, 10.3MB)
테스트 14 〉	통과 (0.33ms, 10.5MB)
테스트 15 〉	통과 (0.49ms, 10.6MB)
테스트 16 〉	통과 (0.86ms, 11MB)
테스트 17 〉	통과 (1.29ms, 11.1MB)
테스트 18 〉	통과 (1.29ms, 11.1MB)
테스트 19 〉	통과 (1.44ms, 11.6MB)
테스트 20 〉	통과 (1.73ms, 11.6MB)
'''