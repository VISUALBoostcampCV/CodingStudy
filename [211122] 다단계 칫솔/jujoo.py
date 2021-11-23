def solution(enroll, referral, seller, amount):
    loc_data = {node : idx for idx, node in enumerate(enroll)}
    result = [0] * len(enroll)
    
    root_list = []
    for leaf in seller:
        tmp = [leaf]
        cur_idx = loc_data[leaf]
        while referral[cur_idx] != '-':
            tmp.append(referral[cur_idx])
            cur_idx = loc_data[referral[cur_idx]]
        tmp.append('center')
        root_list.append(tmp)
    
    for idx, price in enumerate(amount):
        price *= 100
        cur_root = root_list[idx]
        for node in cur_root[:-1]:
            price_10 = int(price * 0.1)
            result[loc_data[node]] += price - price_10
            if price_10 < 1:
                break
            price = price_10
    return result
    
    