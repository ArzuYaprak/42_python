def ft_count_harvest_recursive() -> None:
    number = int(input("Days until harvest: "))

    def helper(i: int) -> None:
        if (i > number):
            return
        print("Day", i)
        helper(i + 1)

    helper(1)
    print("Harvest time!")
