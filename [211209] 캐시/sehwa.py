def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0: # 캐시 사이즈 0일 때 전부 다 cache miss
        return 5*len(cities)
    
    for city in cities:
        city = city.lower() # 대소문자 일치
        if city in cache: # cache hit
            cache.remove(city)
            cache.insert(0,city)
            answer += 1
        else : # cache miss
            if len(cache) == cacheSize: # 캐시가 꽉 찬 경우
                cache.pop()
            cache.insert(0,city)
            answer += 5

    
    return answer


'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.00ms, 10.4MB)
테스트 7 〉	통과 (0.00ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (67.61ms, 17.6MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.06ms, 10.4MB)
테스트 14 〉	통과 (0.08ms, 10.2MB)
테스트 15 〉	통과 (0.13ms, 10.3MB)
테스트 16 〉	통과 (0.18ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.37ms, 10.3MB)
테스트 19 〉	통과 (0.49ms, 10.3MB)
테스트 20 〉	통과 (0.66ms, 10.2MB)

'''