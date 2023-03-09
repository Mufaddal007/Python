
#get user email address
email=input("Please enter your email address-->").strip(" ")

#slice out user name
user=email[0:email.index("@")]


# slice domain name
domain=email[(email.index("@")+1):]

# format message
output="your user name is {} and your domain name is {}".format(user,domain)


#display output message
print(output)

