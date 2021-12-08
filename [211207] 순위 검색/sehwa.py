def solution(infos, queries):
    answer = []
    info_list = []
    query_list = []
    
    for info in infos:
        info_list.append(info.split())

    for query in queries:
        query_list.append(query.split())
    
    for query in query_list:
        for info in info_list:
            for item in query:
                if item == 'and' or '-':
                    continue
                if item == info:
                    pass
                    
            
            
        
    return answer

'''
포기!!!!
'''