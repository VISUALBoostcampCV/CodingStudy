def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize ==0: # 캐시 사이즈가 0일경우 처리
        return 5*len(cities)
        
    for city in cities:
        city = city.upper() # 대소문자 구분X
        
        if city in cache: # cache hit
            answer+=1
            cache.pop(cache.index(city)) # MRU로 갱신
            
        else: # cache miss
            answer+=5
            if len(cache) == cacheSize: # 캐시가 차있을 경우
                cache.pop(0)    #LRU 교체
                
        cache.append(city) # 캐시 저장  
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (63.16ms, 17.5MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.2MB)
테스트 14 〉	통과 (0.15ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.4MB)
테스트 16 〉	통과 (0.16ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.41ms, 10.3MB)
테스트 19 〉	통과 (0.52ms, 10.3MB)
테스트 20 〉	통과 (0.81ms, 10.3MB)
'''