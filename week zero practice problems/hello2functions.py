def main():
    name = input("what's your name? ").strip().title()
    hello(name)

def hello(to = "world"):
    print(f"hello {to}")

main()