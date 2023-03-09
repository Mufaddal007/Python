#Ask user for their name

name=input("Hey there enter your name")

#Ask user for age

age=input("Hey there enter your  age")
#Ask user for city

city=input("Enter your city")

#Ask user what they enjoy

hobby=input("what's your hobby")

#create output text

concat="Hello {} You are {} years old you like {} You live in {}"
output= concat.format(name,age,city,hobby)
#Print output to screen

print(output)
