for number in range(1,12,2):
     print(number)

vowels=0
consonants=0
for letter in "supercalifragilisticexpladocious":
       if letter.lower() in "aeiou":
         vowels=vowels+1

       elif letter==" ":
           pass
       else:
            consonants=consonants+1
            

print("There are {} vowels".format(vowels))
print("there are {} consonants".format(consonants))
