def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        
        if city not in cache: # miss
            if len(cache) == cacheSize: # cache max 일때
                cache.pop(0)
            cache.append(city)
            answer += 5
        elif city in cache: # hit
            cache.append(cache.pop(cache.index(city))) # 인덱싱이 필요하므로 deque를 사용하지 않음
            answer += 1
            
    return answer
  
  '''
  정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (73.00ms, 17.6MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.17ms, 10.3MB)
테스트 15 〉	통과 (0.12ms, 10.2MB)
테스트 16 〉	통과 (0.16ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.39ms, 10.3MB)
테스트 19 〉	통과 (0.63ms, 10.3MB)
테스트 20 〉	통과 (0.71ms, 10.2MB)
'''
