def solution(s):
    answer = []
    
    s = s[1:-1]
    s=s.replace("{", "/")
    s=s.replace("}", "/")    
    
    stack=[]
    arr=[]    
    num =""
    
    for letter in s:
        if letter == "/":
            if num != "":
                stack.append(num)
            if stack:
                arr.append(stack)
            stack=[]
            num=""
        else:
            if letter == ",":
                if num != "":
                    stack.append(num)
                    num = ""
            else:
                num+=letter
    arr = sorted(arr, key=len)
    
    for a in arr:
        for num in a:
            if int(num) not in answer:   
                answer.append(int(num))
                
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.06ms, 10.4MB)
테스트 5 〉	통과 (0.41ms, 10.4MB)
테스트 6 〉	통과 (0.96ms, 10.4MB)
테스트 7 〉	통과 (27.26ms, 11.7MB)
테스트 8 〉	통과 (128.18ms, 15.2MB)
테스트 9 〉	통과 (48.06ms, 12.4MB)
테스트 10 〉	통과 (186.25ms, 15.4MB)
테스트 11 〉	통과 (220.86ms, 17MB)
테스트 12 〉	통과 (342.10ms, 20.1MB)
테스트 13 〉	통과 (332.50ms, 20.3MB)
테스트 14 〉	통과 (391.54ms, 20.3MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
'''