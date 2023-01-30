#create a simple way to store the credentials
#create a way to encode the credentials

import json

#Menu
def Menu():
    i = input('1- Login || 2- Sing up || 3- Quit      :')
    if i == '1':
        login()
    elif i == '2':
        addUser()
    elif i == '3':
        print('Goodbye!')
    else:
        print('not an valid option!')
        Menu()

# reading the json file
def login():
    f = open('credentials.json', 'r')
    dic = json.load(f)
    f.close()
    User = input('Please enter your username:   ')
    pswd = input('Please enter your password:   ')
    try:
        cPswd = dic[User]
        if pswd == cPswd:
            print('successfully loged in!')
        else:
            print('The password is wrong!')
            login()

    except KeyError:
        print('This User does not exist!')
        i = input('Creat a User instead? Y/N')
        if i == 'Y':
            addUser()
        else:
            Menu()

# appending the json file
def addUser():
    f = open('credentials.json', 'r')
    dic = json.load(f)
    f.close()
    User = input('Please enter a new username:  ')
    pswd = input('Please enter a new password:  ')
    pswdConfirmation = input('Please confirm your password: ')

    try:
        dic[User]
        print('user already exist!')
        i = input('Login instead? Y/N')
        if i == 'Y':
            login()
        else:
             Menu()

    except KeyError:
        if pswd == pswdConfirmation:
            dic[User] = pswd
            f = open('credentials.json', 'w')
            f.write(json.dumps(dic, indent=4))
            f.close()
            print('User successfully created!')
        else:
            print('The passwords are not the same.')
            addUser()

Menu()