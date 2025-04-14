'''
A Rainbow Table uses a database of precomputed hashes to
look up the hashed password and then output the text version.
This is used when the attacker already has the uses hashed password.
'''
import hashlib

# Password Hash
hashed_password = '7c6a180b36896a0a8c02787eeafb0e4c'

# table of prcomputed hashes
password_hashes = {
    '5f4dcc3b5aa765d61d8327deb882cf99':'password',
    '1f3870be274f6c49b3e31a0c6728957f':'apple',
    'd8578edf8458ce06fbc5bb76a58c5ca4':'qwerty',
    '7c6a180b36896a0a8c02787eeafb0e4c':'password1'
}

for password_hash in password_hashes:
    print("Trying " + password_hash + " | " + password_hashes[password_hash])
    if password_hash == hashed_password:
        print("Password found: " + password_hashes[password_hash])