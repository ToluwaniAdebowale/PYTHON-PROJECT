#!/usr/bin/env python
# coding: utf-8

# #### QUESTION ONE<br>
# Guess The Number:<br> Write a programme where the computer randomly generates a number between 0 and 20. The user needs to guess what the number is. If the user guesses wrong, tell them their guess is either too high, or too low. 

# In[2]:


import random
random.seed(3)

right_number = random.randint(0, 20)
print("This computer just generated a number")
guessed_number = int(input("Guess the number:"))
if guessed_number == right_number:
    print("Great!!! you guessed the right number")
    
elif guessed_number < right_number:
    print("Nahhh, your guess is too low!")
    
elif guessed_number > right_number:
    print("Ouch!!! your guess is too high")
    
else:
    print("I have no idea of what that is")


# ##### QUESTION TWO:<br>
# Password Generator:<br> Write a programme, which generates a random password for the user. Ask the user how long they want their password to be, and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as numbers and symbols. The password should be a minimum of 6 characters long.

# In[14]:


#random password
#ask for how long the password is, if user requests for less than 6 ask to input more than 6
#ask for how many letters and numbers you want in the password
#password should have a mix of upper and lowercase letters, numbers and symbols
#the password minimun is 6

import random
import string


lengthInput = int(input("How long should your password be?"))



if int(lengthInput) < 6:
    print("The minimum length of the password is 6, please type in the right length!")
    
elif int(lengthInput) >= 6:
    print("This is the right length for a password")
    numberInput = int(input("How many numbers should your password contain?"))
    letterInput = int(input("How many letters should your password contain?"))
    
    def randomPassword(LengthInput, numberInput, letterInput):
        symbolInput=lengthInput-numberInput-letterInput
        halfLetterInput = letterInput//2
        half2LetterInput = letterInput - halfLetterInput
        symbols = [random.choice(string.punctuation) for character in range(symbolInput)]
        lowercases = [random.choice(string.ascii_lowercase) for lower in range(halfLetterInput)]
        uppercases = [random.choice(string.ascii_uppercase) for upper in range(half2LetterInput)]
        numbers = [random.choice(string.digits) for number in range(numberInput)]
        generatedPassword = ''.join(symbols + lowercases + uppercases + numbers)
        return generatedPassword
    
    print(randomPassword(lengthInput, numberInput, letterInput))
    
else:
    print("something is wrong")


# In[ ]:





# In[ ]:




