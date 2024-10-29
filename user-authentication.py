user = {}

def register():
    user_name = input('enter your user name')
    if user_name in user:
        print('user name already exists')
    return

    password = input('enter your password')


user = {
    
} 

def register():
    user_name = input('enter a user name')
    if user_name in user:
        print('pick another name')
    return

full_name = input('enter your full name')
password = input('enter your password')
user['user_name'] = {'fullName': full_name, 'password': password_1}
print('you have succesfully registered')
print(user)

#login function
def login():
    if not user:
        print('user have not registered')
    return
userName = input('enter your user name')
password = input('enter your password')
if user.get(userName) and user[userName]['password'] == password:
    print(f'welcome{user["user_name"]['fullname']}')

def main():
    current_user = None
    while True: 
        print('\n option register login quit')
        choice = input('input an option').lower()

        if choice == 'register':
            register()
        elif choice == login:
            login()
        elif choice == quit:
            ('stopping program')
            break
        else:
            print('invalid input')
        

    main()