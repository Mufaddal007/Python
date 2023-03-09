from random import choice
questions=["why is the sky blue?", "why is there a face on the moon?", "where are all the dinosours?"]

question=choice(questions)
answer=input(question).lower()

while answer!="just because":
      answer=input("why?").strip().lower()
      
