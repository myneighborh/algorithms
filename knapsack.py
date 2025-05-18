# 0-1 Knapsack Problem Solver
# Uses 1D Dynamic Programming

def main():
    n, max_weight = map(int, input().split())
    items = []
    for _ in range(n):
        weight, value = map(int, input().split())
        items.append((weight, value))

    print(knapsack(items, max_weight))


def knapsack(items, max_weight):
    dp = [0] * (max_weight + 1)

    for weight, value in items:
        for w in range(max_weight, weight - 1, -1):
            # if max_weight = 6,
            # 1st weight: 2, value: 10 -> dp = [0, 0, 10, 10, 10, 10, 10]
            # 2nd weight: 3, value: 15 -> dp = [0, 0, 10, 15, 15, 10+15, 10+15]
            # 3rd weight: 1, value: 12 -> dp = [0, 12, 12, 10+12, 15+12, 15+12, 10+15+12]
            dp[w] = max(dp[w], dp[w - weight] + value)

    return max(dp)


if __name__ == "__main__":
    main()