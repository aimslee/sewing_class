import bcrypt
password = b'password123'

hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(8))

print(password)
print(hashed_password)

if bcrypt.checkpw(password, hashed_password):
    print('Passwords match')
else:
    print('Passwords don\'t match')