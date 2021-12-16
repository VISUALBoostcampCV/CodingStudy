def solution(numbers):
    answer = []
    
    
    for number in numbers:
        # 짝수면 +1
        if number % 2 == 0:
            answer.append(number+1)
            continue
        # 홀수면 체크
        answer.append(binary_check(number))
        
    
    return answer


def binary_check(number):
    bin_number = list('0' + bin(number)[2:])
    
    for i in range(len(bin_number)-1, -1, -1):
        if bin_number[i] == '0':
            bin_number[i] = '1'
            bin_number[i+1] = '0'
            break
            
    return int(''.join(bin_number), 2)



'''
테스트 1 〉	통과 (0.66ms, 10.1MB)
테스트 2 〉	통과 (65.49ms, 22.7MB)
테스트 3 〉	통과 (0.08ms, 10MB)
테스트 4 〉	통과 (0.56ms, 10.4MB)
테스트 5 〉	통과 (0.69ms, 10.2MB)
테스트 6 〉	통과 (0.58ms, 10.3MB)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	실패 (런타임 에러)
테스트 10 〉	통과 (312.78ms, 23.7MB)
테스트 11 〉	통과 (325.62ms, 23.6MB)
'''