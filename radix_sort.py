def radix(order):
    is_sorted = False
    position = 1

    while not is_sorted:
        is_sorted = True
        queue_list = [list() for _ in range(10)]

        for num in order:
            digit_number = (int) (num/position) % 10
            queue_list[digit_number].append(num)
            if is_sorted and digit_number > 0:
                is_sorted = False
        idx = 0

        for numbers in queue_list:
            for num in numbers:
                order[idx] = num
                idx += 1
        position *= 10

x = [5,2,4,9,66,32,12]
radix(x)
print(x)