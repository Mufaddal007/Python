films={
     "Finding Dory":[3,5],
     "Bourne":[18,5],
     "Tarzan":[15,3],
     "Ghost Busters":[12,5]
     
    
    }

while True:
    choice=input("Which movie would you like to watch?-->").strip().title()
    if choice in films:
        age=input("How old are you?-->").strip()
        age=int(age)
        if(age>=films[choice][0]):
            num_seats=films[choice][1]
            if num_seats>0:
                
              print("Enjoy the film")
              films[choice][1]=films[choice][1]-1
            else:
                 print("sorry! we are sold out")

        else:
           print("you are too yound to see that film")

               
    else: 
        print("we don't have that film...")
