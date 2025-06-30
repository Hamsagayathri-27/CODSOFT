import random
import string

length =int(input("Enter the length of password="))

if length < 3 :
  print("please enter length more than three characters ")

else :
  password_characters=[random.choice(string.ascii_letters),random.choice(string.digits),random.choice(string.punctuation)]
  all_characters = string.ascii_letters + string.digits + string.punctuation
  password_characters=password_characters + random.choices(all_characters,k=length-3)
  random.shuffle(password_characters)
  password="".join(password_characters)
  print(password)

