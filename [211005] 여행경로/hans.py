from collections import defaultdict

def dp(n, map, start, from_, path):
    
    results = ['ZZZ']
    for end in map[start]:
        if map[start][end] == 0:    #if don't go
            continue
        map[start][end] -= 1        #delete one ticket
        new_path = path+'/'+end     #for a large comparison, use a string
        # print(new_path)
        # print(map)
        
        if len(new_path)==n:        #back
            map[start][end] += 1
            map[from_][start] += 1
            # print(map)
            return new_path

        results.append(dp(n, map, end, start, new_path))
                    
    map[from_][start] += 1          #back
    return min(results)


def solution(tickets):
    n = len(tickets)
    n = n+3*(n+1)
    
    map = defaultdict(lambda: defaultdict(int))
    
    for start, end in tickets:      #create map
        map[start][end] += 1
    print(f"map : {map}")
    return dp(n, map, 'ICN', "ICN", 'ICN')

a = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
b = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
c = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]

answer = solution(c)
print(f'answer is {answer}')


'''
테스트 1 〉	통과 (44.52ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
'''