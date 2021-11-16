def solution(n, results):
    answer = 0
    
    ranks = [[0]*n for _ in range(n)]
    # print(rank)
    
    for result in results:
        w, l = result
        ranks[w-1][l-1] ,ranks[l-1][w-1]= 1, -1
    
    
    print(ranks)
    for rank in ranks:
        for i in range(n):
            if rank[i] == 1:
                for j in range(n):
                    if ranks[i][j] == 1:
                        rank[j] = 1
            elif rank[i] == -1:
                for j in range(n):
                    if ranks[i][j] == -1:
                        rank[j] = -1
    
    print(ranks)
    
    for rank in ranks:
        if rank.count(0) == 1:
            answer+=1
    
    return answer
  
  '''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	실패 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (1.95ms, 10.3MB)
테스트 6 〉	통과 (5.87ms, 10.3MB)
테스트 7 〉	실패 (18.82ms, 10.3MB)
테스트 8 〉	실패 (64.69ms, 10.5MB)
테스트 9 〉	실패 (68.04ms, 10.6MB)
테스트 10 〉	통과 (116.68ms, 10.6MB)
'''
