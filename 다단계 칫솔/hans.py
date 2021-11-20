def distribution(d, name, amount):
    amount_send = amount//10
    d[name][1] += amount-amount_send
    if amount_send>0 and d[name][0]!='-':
        distribution(d, d[name][0], amount_send)
        
def solution(enroll, referral, seller, amount):
    answer = []
    d = dict()  # referral dict
    for i, name in enumerate(enroll):
        d[name] = [referral[i], 0]
            
    for i, name in enumerate(seller):
        distribution(d, name, amount[i]*100)
        
    for name in enroll:
        answer.append(d[name][1])
    
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

s = solution(enroll,referral,seller,amount)
print(s)

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.16ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (1.19ms, 10.3MB)
테스트 6 〉	통과 (3.94ms, 12.9MB)
테스트 7 〉	통과 (4.04ms, 12.8MB)
테스트 8 〉	통과 (5.30ms, 13MB)
테스트 9 〉	통과 (18.95ms, 14.1MB)
테스트 10 〉	통과 (142.27ms, 21.2MB)
테스트 11 〉	통과 (129.98ms, 20.6MB)
테스트 12 〉	통과 (123.38ms, 20.6MB)
테스트 13 〉	통과 (129.71ms, 20.6MB)

'''