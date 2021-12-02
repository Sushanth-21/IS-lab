import pyDes
plain=input("Enter plain text : ").encode()
k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
cipher=k.encrypt(plain)
decrypt=k.decrypt(cipher)
print("Encrypted data is : ",cipher)
print("Decrypted data is : ",decrypt.decode())