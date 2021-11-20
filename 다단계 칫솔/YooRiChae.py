def solution(enroll, referral, seller, amount):
    def dp(person, money):
        if money == 0:
            return
        idx = info[person][1]
        
        if info[person][0] != "-":
            dp(info[person][0], money//10)
        answer[idx] = answer[idx] + (money - money//10)
        
    answer=[]    
    for _ in range(0, len(enroll)):
        answer.append(0)
        
    info ={}
    for idx, person in enumerate(enroll):
        info[person] = (referral[idx], idx)
    
    for idx, person in enumerate(seller):
        dp(person, amount[idx]*100)
        
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.16ms, 10.4MB)
테스트 5 〉	통과 (1.33ms, 10.3MB)
테스트 6 〉	통과 (3.67ms, 13.6MB)
테스트 7 〉	통과 (3.55ms, 13.7MB)
테스트 8 〉	통과 (5.25ms, 13.9MB)
테스트 9 〉	통과 (20.47ms, 15MB)
테스트 10 〉	통과 (195.69ms, 22.1MB)
테스트 11 〉	통과 (154.75ms, 21.5MB)
테스트 12 〉	통과 (152.91ms, 21.4MB)
테스트 13 〉	통과 (168.95ms, 21.4MB)
'''