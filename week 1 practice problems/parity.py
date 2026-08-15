def main():
    x = float(input("What's x?"))
    if is_even(x):
        print(f"{x} is even")
    
    elif x.is_integer():
        print(f"{x} is odd")
    
    else:
        print(f"{x} is not an integer")
    
def is_even(n):
    return n % 2 == 0
    
main()