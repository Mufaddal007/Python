known_users=["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]
print(len(known_users))
while 1:
    print("My name is TRAVIS")
    name=input("What is your name?--->").strip(" ").capitalize()
    if name in known_users:
            print("Hello! {}".format(name))
            remove=input("would you like to be removed from teh system? Y/N").strip().lower()
            if remove=="y":
               known_users.remove(name)
               print("Your name is removed successfully")

            else :
                print("No problem, I didn't want you to leave anyway")
    else:
        print("I don't think I have met you yet {}".format(name))
        addme=input("would you like to be added to the system? Y/N").strip().lower()
        if addme=="y":
              known_users.append(name)
              print("Your name is  successfully added to the recognized name list")      
        else:
              print("no worries see you around")
          
