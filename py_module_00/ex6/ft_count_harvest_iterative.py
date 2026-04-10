def ft_count_harvest_iterative():
    harvest = int(input("Days until harvest: "))
    for day in range(1, harvest + 1):
        print(f'Day {day}')
    print("Harvest time!")
