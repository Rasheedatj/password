myPassword = 'dorcas'

userPassword = input('Enter your password \n').lower()

if(userPassword == myPassword):
    print('login sucessful!')
else:
    print('incorrect password, try again!')