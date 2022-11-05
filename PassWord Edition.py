from cryptography.fernet import Fernet

#print('Welcome to password manager.')
MasterPassword = input('Enter your Password master: ').lower()

if MasterPassword != 'raja':
    print('You entered incorrect Password master.')
    quit()
else:
    pass


def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


key = load_key() + MasterPassword.encode()
fer = Fernet(key)


def add():
    #account = input('What is the account name?: ')
    Username = input('Enter your username here: ')
    password = input('Enter your password: ')
    account = input(
        'what account for which you want to save the credentials? ')
    with open('Passwords.txt', 'a') as f:
        f.write(f'\nACCOUNT:{account.upper()}\n')
        f.write(f'\nUsername: {Username}\nPassword: {fer.encrypt(password.encode()).decode()}\n')
        print('')


def view():
    with open('Passwords.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line.startswith('ACCOUNT'):
                ac = line.split(':')
                print('')
                print(ac[1])
            elif line.startswith('Username'):
                words = line.split(':')
                print(f'Username: {words[1]}')

            elif line.startswith('Password'):
                passw = line.split(':')
                print(f'Password: {fer.decrypt(passw[1].encode()).decode()}')
                print('')
            
while True:
    need = input(
        'Would want to add or view the alread existing passwords? type(view/Add) or q to quit: ').lower()
    if need == 'q':
        break

    if need == 'add':
        add()

    elif need == 'view':
        view()
    else:
        print('Please specify if you want to view or add.')
        continue
