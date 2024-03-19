# Name: Luke Kutz-Pears
# Date: 03/19/2024

# function to decode an encoded password.
def decode_password(encoded_password):
    decoded_pass = ''
    for i in encoded_password:
        decoded_pass += str(int(i) - 3)
    return int(decoded_pass)