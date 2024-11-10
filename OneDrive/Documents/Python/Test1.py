def solution(A):
    # Convert the array to a set for fast lookups
    numbers = set(A)
    
    # Start looking for the smallest positive integer starting from 1
    smallest_missing = 1

    # Iterate until we find a missing integer
    while smallest_missing in numbers:
        smallest_missing += 1

    return smallest_missing

print(solution([1, 3, 6, 4, 1, 2]))  # Output: 5
print(solution([1, 2, 3]))            # Output: 4
print(solution([-1, -3]))             # Output: 1
print(solution([2, 3, 4, 5]))         # Output: 1
print(solution([0, 1, 2, 5]))         # Output: 3
