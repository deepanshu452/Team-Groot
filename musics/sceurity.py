import random
import string

def get_security_key():
    chars = string.ascii_letters + string.digits + string.punctuation
    secret_key = ''.join(random.choice(chars) for _ in range(50))
    return secret_key