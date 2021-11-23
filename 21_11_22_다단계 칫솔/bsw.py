from collections import defaultdict

def move_parent(tree, name, money):
    if name in tree:
        if money == 0: # 무한루프 방지
            return
        tree[name]['money'] += money - int(money*0.1)
        move_parent(tree, tree[name]['parent'], int(money*0.1))
    
    
def solution(enroll, referral, seller, amount):
    answer = []
    
    tree = defaultdict(dict)
    
    for i, v in enumerate(enroll):
        tree[v]['parent'] = referral[i]
        tree[v]['money'] = 0
        
    for i, name in enumerate(seller):
        move_parent(tree, name, amount[i]*100)
        
    
    return list(tree[name]['money'] for name in enroll)
  
  
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.14ms, 10.3MB)
테스트 3 〉	통과 (0.11ms, 10.3MB)
테스트 4 〉	통과 (0.37ms, 10.3MB)
테스트 5 〉	통과 (1.84ms, 10.3MB)
테스트 6 〉	통과 (6.03ms, 14.4MB)
테스트 7 〉	통과 (6.76ms, 14.5MB)
테스트 8 〉	통과 (8.70ms, 14.5MB)
테스트 9 〉	통과 (32.05ms, 15.7MB)
테스트 10 〉	통과 (259.40ms, 22.7MB)
테스트 11 〉	통과 (239.74ms, 22.1MB)
테스트 12 〉	통과 (234.11ms, 22.1MB)
테스트 13 〉	통과 (203.86ms, 22.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
