import hashlib

print hashlib.md5(hashlib.sha256("id0-rsa.pub").hexdigest()).hexdigest()
