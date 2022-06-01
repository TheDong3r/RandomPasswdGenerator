# Mini Project - Random Password Generator!

# Importing the relevant modules
from random import randint

# Upper and lowercase password
password = ""
for i in range(5):
    i = chr(randint(65, 90))
    j = chr(randint(65, 90)).lower()
    k = randint(0,10)
    password = str(password) + i + j + str(k)
print(password)

