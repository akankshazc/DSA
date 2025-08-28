def grid_traveller_memo(m: int, n: int, memo={}):
    key = f"{m},{n}"

    if key in memo.keys():
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveller_memo(
        m-1, n, memo) + grid_traveller_memo(m, n-1, memo)

    return memo[key]


if __name__ == "__main__":
    print(grid_traveller_memo(1, 1))  # 1
    print(grid_traveller_memo(2, 3))  # 3
    print(grid_traveller_memo(3, 2))  # 3
    print(grid_traveller_memo(3, 3))  # 6
    print(grid_traveller_memo(18, 18))  # 2333606220
