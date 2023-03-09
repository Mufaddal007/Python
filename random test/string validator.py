s=input("enter a string")

cases=["False","False","False","False","False"]

for x in s:
    if x.isalnum():
        cases[0]="True"
        break
for x in s:
    if x.isalpha():
        cases[1]="True"
        break
for x in s:
    if x.isdigit():
        cases[2]="True"
        break
for x in s:
        if x.islower():
        cases[3]="True"
        break
for x in s:
    if x.isupper():
        cases[4]="True"
        break

for y in cases:
    print(y)
