def main():
    i = ask_number()
    roar(i)

def roar(a):
    for _ in range(a):
        print("Roar")

def ask_number():

    n = int(input("How many times do you want to roar?"))

    return n



main()