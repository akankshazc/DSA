def can_sum(target_sum: int, numbers: list):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers) == True:
            return True

    return False


if __name__ == "__main__":
    print(can_sum(7, [2, 3]))  # True
    print(can_sum(7, [5, 3, 4, 7]))  # True
    print(can_sum(7, [2, 4]))  # False
    print(can_sum(8, [2, 3, 5]))  # True
    # Problem with this:
    print(can_sum(300, [7, 14]))  # False
