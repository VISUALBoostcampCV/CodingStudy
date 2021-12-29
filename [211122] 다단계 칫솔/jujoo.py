class Sell:
    def __init__(self, enroll, referral, seller, amount):
        self.answer = [0] * len(enroll)
        self.referral = referral
        self.enroll_idx = {val : idx for idx, val in enumerate(enroll)}
        for cur_seller, cur_amount in zip(seller, amount):
            self.dfs(cur_seller, cur_amount * 100)
    def dfs(self, cur_seller, cur_amount):
        if cur_amount < 1 or cur_seller == '-':
            return
        cur_idx = self.enroll_idx[cur_seller]
        self.answer[cur_idx] += cur_amount - int(cur_amount * 0.1)
        self.dfs(self.referral[cur_idx], int(cur_amount * 0.1))

def solution(enroll, referral, seller, amount):
    sell = Sell(enroll, referral, seller, amount)
    return sell.answer