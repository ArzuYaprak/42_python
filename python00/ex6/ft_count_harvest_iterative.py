def ft_count_harvest_iterative() -> None:
    number = int(input("Days until harvest: "))
    for i in range(1, number + 1):
        print("Day", i)
    print("Harvest time!")
