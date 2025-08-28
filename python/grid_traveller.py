def grid_traveller(m: int, n: int):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    return grid_traveller(m-1, n) + grid_traveller(m, n-1)


if __name__ == "__main__":
    print(grid_traveller(1, 1))  # 1
    print(grid_traveller(2, 3))  # 3
    print(grid_traveller(3, 2))  # 3
    print(grid_traveller(3, 3))  # 6
    print(grid_traveller(18, 18))  # 2333606220
