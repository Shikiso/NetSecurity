'''
A dictionary attack uses a list of common passwords
and checks each one against the hashed password.
'''
import hashlib

# Password Hash
hashed_password = '7c6a180b36896a0a8c02787eeafb0e4c'

# Create table of hashed passwords
# -------------------------------------
# Getting list of possible passwords
file = open("passwords.txt", "r")
passwords = file.read()
file.close()

# Creating hashed versions of the passwords and storing them in a dictionary
hashes = {}
for password in passwords.split("\n"):
    hash = hashlib.md5(password.encode('utf-8')).hexdigest()
    hashes[hash] = password

# Compares hashed passwords against password hash
for hash in hashes:
    print("Testing " + hash)
    if hash == hashed_password:
        print("Password Found: " + hashes[hash])
        break