import string
from random import randint

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
characters_list = [character for character in characters]

length = int(input('how long you want your new password?\n> ')) + 1

passwd = []

for i in range(1, length):
    passwd.append(characters_list[randint(0, len(characters_list) - 1)])

passwd_text = ''.join(passwd)
print(passwd_text)
