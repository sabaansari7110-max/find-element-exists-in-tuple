#create a list of numbers
numbers= [10,20,30,40,50]

#take input from the user
element= int(input("enter a number:"))

#check if the element exists in the list
if element in numbers:
    print("element exists in the tuple")
else:
    print("element does not exists in the tuple")