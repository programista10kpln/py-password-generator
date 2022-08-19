import string
from random import randint

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
characters_list = [character for character in characters]

length = input('how long you want your new password?\n> ')
