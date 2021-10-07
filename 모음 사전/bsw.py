from itertools import combinations_with_replacement, product

def solution(word):
    answer = 0
    
    alpha = 'AEIOU'
    
    dic = []
    for i in range(1, 5 +1):
        dic.extend(combinations_with_replacement(alpha, i))
        
    products = set()
    for i, d in enumerate(dic):
        products.update(product(d, repeat=len(d)))
        
    products = sorted(list(products))
    tuple2str = []
    for p in products:
        tuple2str.append(''.join(p))
        
    return tuple2str.index(word) +1
