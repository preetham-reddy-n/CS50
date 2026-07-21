def hello(to):
    print(f"hello, {to}")

name = input("what's your name? ").strip().title()
hello(name)