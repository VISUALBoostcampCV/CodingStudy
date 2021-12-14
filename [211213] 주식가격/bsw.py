def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i, len(prices)):
          # 모든 idx마다 검사
            if(prices[i] > prices[j]):
                answer.append(j-i)
                break
            elif(j==len(prices)-1):
                answer.append(j-i)
    
    return answer
