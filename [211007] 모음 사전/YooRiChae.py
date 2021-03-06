def test(word, vowels, w, words):
    if len(w) == 5:
        w=w[:-1]
        return
    
    for letter in vowels:
        w+=letter
        words.append(w)
        test(word,vowels,w,words)
        w=w[:-1]
        
def solution(word):
    vowels =['A', 'E', 'I', 'O', 'U']
    words = []
    w=''
    test(word, vowels, w, words)
    answer = words.index(word)+1
    return answer

'''
테스트 1 〉	통과 (1.32ms, 10.4MB)
테스트 2 〉	통과 (1.64ms, 10.3MB)
테스트 3 〉	통과 (1.52ms, 10.4MB)
테스트 4 〉	통과 (1.33ms, 10.3MB)
테스트 5 〉	통과 (1.33ms, 10.3MB)
테스트 6 〉	통과 (1.31ms, 10.3MB)
테스트 7 〉	통과 (1.33ms, 10.3MB)
테스트 8 〉	통과 (1.38ms, 10.3MB)
테스트 9 〉	통과 (1.27ms, 10.3MB)
테스트 10 〉	통과 (1.32ms, 10.3MB)
테스트 11 〉	통과 (1.33ms, 10.3MB)
테스트 12 〉	통과 (1.34ms, 10.3MB)
테스트 13 〉	통과 (1.46ms, 10.3MB)
테스트 14 〉	통과 (1.35ms, 10.3MB)
테스트 15 〉	통과 (1.27ms, 10.3MB)
테스트 16 〉	통과 (1.36ms, 10.3MB)
테스트 17 〉	통과 (1.37ms, 10.2MB)
테스트 18 〉	통과 (1.27ms, 10.3MB)
테스트 19 〉	통과 (1.30ms, 10.3MB)
테스트 20 〉	통과 (1.36ms, 10.3MB)
테스트 21 〉	통과 (1.30ms, 10.3MB)
테스트 22 〉	통과 (1.26ms, 10.3MB)
테스트 23 〉	통과 (1.24ms, 10.3MB)
테스트 24 〉	통과 (1.50ms, 10.3MB)
테스트 25 〉	통과 (1.27ms, 10.3MB)
테스트 26 〉	통과 (1.33ms, 10.3MB)
테스트 27 〉	통과 (1.30ms, 10.3MB)
테스트 28 〉	통과 (1.44ms, 10.3MB)
테스트 29 〉	통과 (1.40ms, 10.3MB)
테스트 30 〉	통과 (1.31ms, 10.3MB)
테스트 31 〉	통과 (1.28ms, 10.3MB)
테스트 32 〉	통과 (1.40ms, 10.3MB)
테스트 33 〉	통과 (1.40ms, 10.3MB)
테스트 34 〉	통과 (1.29ms, 10.3MB)
테스트 35 〉	통과 (1.33ms, 10.3MB)
테스트 36 〉	통과 (1.38ms, 10.3MB)
테스트 37 〉	통과 (1.36ms, 10.3MB)
테스트 38 〉	통과 (1.35ms, 10.3MB)
테스트 39 〉	통과 (1.26ms, 10.3MB)
테스트 40 〉	통과 (1.26ms, 10.4MB)
'''