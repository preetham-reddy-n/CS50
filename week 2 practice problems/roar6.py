def main():
    i = ask_number()
    roar(i)

def roar(a):
    for _ in range(a):  #a loop variable here, but I don't care what its value is.
        print("Roar")

def ask_number():

    while True:
        n = int(input("How many times do you want to roar?"))
        if n > 0:
            break

    return n



main()