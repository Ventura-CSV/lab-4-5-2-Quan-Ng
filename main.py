import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while total <= 100:
            rand_num = random.randint(1, 20)
            numbers.append(rand_num)
            total += rand_num
            
    if total > 100:
        last_number = numbers.pop()
        total -= last_number


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
