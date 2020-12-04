import os
import base64
import hashlib
# b'U\xf7+\xe9=4\xbd\xd1\xf3\xd7$\xa2\xa7H\xbe\xc5'
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


m = hashlib.sha256()
m.update(b"Nobody inspes")

l = m.digest()
print(l)