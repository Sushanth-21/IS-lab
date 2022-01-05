import pyDes
plain=input("Enter plain text : ").encode()
key=input("Enter key of size 8 : ").encode()
k = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
cipher=k.encrypt(plain)
decrypt=k.decrypt(cipher)
print("Encrypted data is : ",cipher)
print("Decrypted data is : ",decrypt.decode())
