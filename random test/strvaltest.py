str1="aksn  _-45t@9983.com"
username=str1[:str1.index("@")]
website=str1[str1.index("@")+1:str1.index(".")]
extension=str1[str1.index(".")+1:]
stg = ["_","-"]
print(username)
print(website)
print(extension)

for x in username:
    if x.isalnum() or x in stg:
        print("True")
for x in website :
    if x.isalnum() :
        print("True")
        
