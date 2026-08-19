def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#")



#instead of for loop we can also use :

    #print("#\n" * height, end="")

main()