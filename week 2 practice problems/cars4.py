#the program where dicyionary is first used used by me 


cars = {"Centodieci": "Buggati" , 
         "Supra" : "Toyota", 
         "Boat Tail" : "Rolls Royce", 
         "Zonda" : "Pagani", 
         "Jesko" : "Konisegg",
          "9  11" : "Porsche"}



for company in cars.values(): #.values is used for getting the value in the dictionay
    print(company)




#The for loop can also be written as:
#for car, company in cars.items():
# print(car, company) # this will print both the key and the value in the dictionary.


#It can also be written as:
#for car in cars:
# print(car, cars[car]) # this will also print both the key and the value in the dictionary.