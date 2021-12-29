def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = str(bin(number)[2:])
        if bin_number[-2:] in ['00', '10', '01'] or number in [0, 1]:
            answer.append(number + 1)
        else:
            # reversed(range(2, len(bin_number) + 1)) = [3, 2]
            for i in reversed(range(2, len(bin_number) + 1)):
                # i = 3, number = 7
                # bin_number[-i:] = 111
                if '0' not in bin_number[-i:]:
                    answer.append(number + 2**(i - 1))
                    break
    return answer

print(solution([0, 555, 123, 100000, 99999, 1000000000, 999999999999, 10**15, 10**15 -1]))