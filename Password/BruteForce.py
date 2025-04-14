'''
A Brute Force Attack uses the machines resouces to try every
possible combination of available characters, numbers and symbols
to guess the password.

For this example I'm only going to use lowcase letters and numbers
so that it doesn't take so long. I'm also only using 3 characters.

It would be better to use a faster language like c++ but this is the 
basics anyway
'''
import hashlib, time

# Password Hash (Feel free to change the 'abc' to something else)
# (just make sure it's only 3 characters and lower case letters and numbers)
hashed_password = hashlib.md5('2d7'.encode('utf-8')).hexdigest()

characters = [i for i in 'abcdefghijklmnopqrstuvwxyz1234567890']

start = time.time() # Timer
# Brute force alorithm
for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                password_attempt = char1+char2+char3
                hash = hashlib.md5(password_attempt.encode('utf-8')).hexdigest()
                if hash == hashed_password:
                    print("Password Found: " + password_attempt)
                    end = time.time() # End timer
                    print("Took " + str(end-start) + "ms")