def solution(n, results):
    answer = 0
    d = [{'w':[],'l':[]} for i in range(n)] # 승, 패를 저장하는 dict

    for w,l in results:
        d[w-1]['w'].append(l-1)
        d[l-1]['l'].append(w-1)

    def dp(lst, w_or_l, history):   # dp를 사용하여 내가 이긴애가 이긴애, 내가 진애가 진애들을 전부 탐색
        for l in lst:
            if l not in history:
                history.append(l)
                dp(d[l][w_or_l],w_or_l,history)
        return history

    for p in range(n):
        res = dp(d[p]['w'],'w',[]) + dp(d[p]['l'],'l',[]) # 내가 이긴애가 이긴애 + 내가 진애가 진애
        if len(res)==n-1:
            answer += 1
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (1.07ms, 10.3MB)
테스트 6 〉	통과 (2.34ms, 10.3MB)
테스트 7 〉	통과 (17.38ms, 10.4MB)
테스트 8 〉	통과 (61.86ms, 10.6MB)
테스트 9 〉	통과 (89.51ms, 10.7MB)
테스트 10 〉통과 (94.74ms, 10.5MB)

'''