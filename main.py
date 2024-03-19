#encode function adds 3 to each character in an 8 number string and returtns resulting string
def encode_password(password):
    encoded = ''
    for i in range(8):
        y = int(password[i])
        y += 3
        y = str(y)
        encoded = encoded + y
    return encoded
#main function outputs menu in while loop until user selects option to quit
if __name__  == '__main__':
    user_quit = False
    while user_quit == False:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        option = int(input('Please enter an option: '))
        #stores user input as original_password and creates encoded_password with encode function above
        if option == 1:
            original_password = input('Please enter your password to encode: ')
            encoded_password = encode_password(original_password)
            print('Your password has been encoded and stored!')
            print('')
        #outputs encoded and original passwords created in option 1
        if option == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}.')
            print('')
        #exits the loop and ends the program
        if option == 3:
            user_quit = True

