#The computer introduces itself
name = input("Hey, I am computer, what's your name ").strip().title()

#Splitting the name into first and last name
first, last = name.split(" ")

#The computer greets user
print (f"Hello, {first}")