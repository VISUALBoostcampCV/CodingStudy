def solution(n, times):
    answer = 0
    left, right = 0, max(times) * n

    while left < right:
        mid = (right + left) // 2
        # mid = left + (right - left) // 2

        if sum([mid // t for t in times]) >= n:
            right = mid
        else:
            left = mid + 1

    return left