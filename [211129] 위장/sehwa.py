def solution(clothes) :
    answer = 1
    type_list = {}
    
    for i in range(len(clothes)) :
        temp = type_list.get(clothes[i][1])
        if temp :
            temp += 1
            type_list[clothes[i][1]] = temp
        else :
            type_list[clothes[i][1]] = 1
            
    print(type_list)
    
    for value in type_list.values():
        answer = (value+1)*answer
    
    return answer-1