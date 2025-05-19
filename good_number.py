# Two Pointer

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers)
    print(check_is_good(n, numbers))


def check_is_good(n, numbers):
    count = 0

    for i in range(n):
        target = numbers[n]
        left = 0
        right = n - 1
        
        while left < right:
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue

            total = numbers[left] + numbers[right]

            if total == target:
                count += 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return count
            

if __name__ == "__main__":
    main()