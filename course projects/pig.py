#get sentence from user

original=input("type a sentence").strip().lower()

#split sentence into words
words=original.split()
#loop through words and convert to pig latin
new_words=[]
#stick words baack together
for word in words:
    
    if word[0] in "aeiou":
       new_word=word+"yay"
       new_words.append(new_word)
    else:
        vowel_pos=0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos=vowel_pos+1
            else:
                break
            
        cons=word[:vowel_pos+1]
        the_rest=word[vowel_pos:]
        new_word=the_rest+cons+"ay"
        new_words.append(new_word)
     
#output the final string
output=" ".join(new_words)
print(output)
