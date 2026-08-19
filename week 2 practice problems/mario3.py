def main():
    print_square(3)


def print_square(size):
    #for each row of bricks

    for x in range(size):


        # for each brick in row
        for y in range(size):
           print("#", end="")
        print()




     #   for _ in range(size):
     #     print("#" * size)


main()