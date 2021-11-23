from collections import defaultdict

def solution(enroll, referral, seller, amount):
    ref_dict = {}
    profit_dict = defaultdict(int)    
    
    # 구성원: 추천인 으로 딕셔너리 구성
    for e, r in zip(enroll, referral):        
        ref_dict[e] = r
    
    # 이익 배분하는 함수
    def profit_calculate(seller, profit):        
        # 추천인 혹은 center에 줘야 하는 돈
        offer = profit // 10       
        
        # 원 단위로 절사했는데 줄 돈이 없을 경우 가지고 끝냄
        if not offer:
            profit_dict[seller] += profit
            return
                    
        profit_dict[seller] += profit - offer
        
        # 자신을 추천한 직원이 없는 경우
        if ref_dict[seller] == '-':
            # 끝냄
            return
        
        # 추천한 직원이 있는 경우
        else:
            profit_calculate(ref_dict[seller], offer)        
        
        
    # 이익 배분 시작
    for s, a in zip(seller, amount):
        profit_calculate(s, a * 100)
    
    answer = [profit_dict[e] for e in enroll]   
        
    
    return answer


'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.08ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.26ms, 10.3MB)
테스트 5 〉	통과 (1.79ms, 10.3MB)
테스트 6 〉	통과 (2.56ms, 13.1MB)
테스트 7 〉	통과 (4.48ms, 13MB)
테스트 8 〉	통과 (4.18ms, 13MB)
테스트 9 〉	통과 (15.89ms, 14.3MB)
테스트 10 〉	통과 (148.89ms, 21.4MB)
테스트 11 〉	통과 (111.96ms, 20.6MB)
테스트 12 〉	통과 (115.08ms, 20.6MB)
테스트 13 〉	통과 (100.93ms, 20.5MB)
'''