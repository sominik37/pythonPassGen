import random
import string

#passgen dunction

def PassGen(length):
    ran = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    print(ran)
length = random.randint(8, 15)
PassGen(length)