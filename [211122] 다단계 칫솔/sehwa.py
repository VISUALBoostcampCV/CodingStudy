def to_dict(key_list, val_list):
    calc_dict = {}
    for k,v in zip(key_list, val_list):
        calc_dict[k] = v
    return calc_dict

def solution(enroll, referral, seller, amount):
    answer = []
    
    enroll_tree = to_dict(enroll, referral)
    seller_tree = to_dict(seller, amount*100)
    
    for e in enroll :
        if e not in referral:
            seller_tree[e] = seller_tree[e] * 0.9
            if enroll_tree[e] in seller_tree.keys():
                seller_tree[enroll_tree[e]] += seller_tree[e] * 0.1
            else:
                seller_tree[enroll_tree[e]] = seller_tree[e] * 0.1
            
            #### 빠져나오는 방법????!?!?
    
    
    return answer